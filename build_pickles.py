import os
import pickle
import argparse

import pandas as pd
from pathlib import Path
from utils import convert_to_dataset

from torchtext import data as ttd
from soynlp.word import WordExtractor
from soynlp.tokenizer import LTokenizer


os.environ['CUDA_LAUNCH_BLOCKING'] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def build_tokenizer():
    """
    Train soynlp tokenizer which will be used to tokenize Korean input sentence
    """
    print(f'Now building soy-nlp tokenizer . . .')

    data_dir = Path().cwd() / 'data'
    train_file = os.path.join(data_dir, 'corpus.csv')

    df = pd.read_csv(train_file, encoding='utf-8')

    # if encounters non-text row, we should skip it
    kor_lines = [row.korean
                 for _, row in df.iterrows() if type(row.korean) == str]

    word_extractor = WordExtractor(min_frequency=5)
    word_extractor.train(kor_lines)

    word_scores = word_extractor.extract()
    cohesion_scores = {word: score.cohesion_forward
                       for word, score in word_scores.items()}

    with open('pickles/tokenizer.pickle', 'wb') as pickle_out:
        pickle.dump(cohesion_scores, pickle_out)


def build_vocab(config):
    """
    Build vocab used to convert input sentence into word indices using soynlp and spacy tokenizer
    Args:
        config: configuration containing various options
    """
    pickle_tokenizer = open('pickles/tokenizer.pickle', 'rb')
    cohesion_scores = pickle.load(pickle_tokenizer)
    tokenizer = LTokenizer(scores=cohesion_scores)

    # include lengths of the source sentences to use pack pad sequence
    kor = ttd.Field(tokenize=tokenizer.tokenize,
                    lower=True,
                    batch_first=True)

    jeju = ttd.Field(tokenize=tokenizer.tokenize,
                    init_token='<sos>',
                    eos_token='<eos>',
                    lower=True,
                    batch_first=True)

    data_dir = Path().cwd() / 'data'
    train_file = os.path.join(data_dir, 'train.csv')
    train_data = pd.read_csv(train_file, encoding='utf-8')
    train_data = convert_to_dataset(train_data, kor, jeju)

    print(f'Build vocabulary using torchtext . . .')

    kor.build_vocab(train_data, max_size=config.kor_vocab)
    jeju.build_vocab(train_data, max_size=config.jeju_vocab)

    print(f'Unique tokens in Korean vocabulary: {len(kor.vocab)}')
    print(f'Unique tokens in Jeju vocabulary: {len(jeju.vocab)}')

    print(f'Most commonly used Korean words are as follows:')
    print(kor.vocab.freqs.most_common(20))

    print(f'Most commonly used Jeju words are as follows:')
    print(jeju.vocab.freqs.most_common(20))

    with open('pickles/kor.pickle', 'wb') as kor_file:
        pickle.dump(kor, kor_file)

    with open('pickles/jeju.pickle', 'wb') as jeju_file:
        pickle.dump(jeju, jeju_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pickle Builder')

    parser.add_argument('--kor_vocab', type=int, default=70000)
    parser.add_argument('--jeju_vocab', type=int, default=120000)

    config = parser.parse_args()

    build_tokenizer()
    build_vocab(config)
