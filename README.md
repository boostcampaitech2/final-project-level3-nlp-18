# final-project-level3-nlp-18
final-project-level3-nlp-18 created by GitHub Classroom


# How to use fairseq translation model

## Requirements 
  python >= 3.6  
  NumPy >= 1.11.1    
  Sentencepiece   
  tqdm   
## Practice
  <pre><code>
  git clone https://github.com/pytorch/fairseq.git
  cd fairseq
  pip install --editable ./ 
 </pre></code>
  1. Input files in your fairseq folder
  2. Make JIT folder and input your data 

   <pre><code>
   #BPE segments for training
    python bpe_segment.py --jit jit --vocab_size 4000
    
   #Fairseq prepro
    python prepro.py --src je --tgt ko --vocab_size 4000
    python prepro.py --src ko --tgt je --vocab_size 4000
    
    
   #Training
    bash train_koje.sh
    bash train_jeko.sh
    
   #Interactive mode (외부 문장에 대한 생성과 입출력에 쓰인다)
    bash interactive.sh
    
   #Score (Src 문장을 넣으면 모델을 돌려 Tgt 문장에 대한 해석된 문장의 점수를 계산한다)
    bash generate_koje.sh
    bash generate_jeko.sh
   
   #Backtranslation
    1. je->ko 베이스라인 모델 학습
      python bpe_segment.py --jit jit --vocab_size 4000
      python prepro.py --src je --tgt ko --vocab_size 4000
      bash train_jeko.sh
    2. ko->je backtranslate용 모델 학습
      python prerpor.py --src ko --tgt je --vocab_size 4000
      bash train_koje.sh
    3. 2번 모델을 사용해 단일 표준어 데이터에서 제주어를 생성를 만들어 한쌍의 데이터 제작
      python prepro.py --src exteranl --tgt je --vocab_size 4000
      bash generate_ex2je.sh
    4. 1~3의 모든 데이터를 이용해 학습
    

  </pre></code>
