# final-project-level3-nlp-18
final-project-level3-nlp-18 created by GitHub Classroom


# How to use fairseq translation model

## Requirements 
  python >= 3.6  
  NumPy >= 1.11.1  
  Fairseq   
  Sentencepiece   
  tqdm   
## Practice
  1. git clone https://github.com/pytorch/fairseq.git
  2. cd fairseq
  3. pip install --editable ./  
  4. Input bash files 
  5. Put JIT folder 
  6. Download prepro.py and bpe_segment.py form https://github.com/kakaobrain/jejueo/tree/master/translation
   <pre><code>
   #BPE segments for training
    python bpe_segment.py --jit jit --vocab_size 4000
    
   #Fairseq prepro
    python prepro.py --src ko --tgt je --vocab_size 4000
    python prepro.py --src je --tgt ko --vocab_size 4000
    
   #Training
    bash train_koje.sh
    bash train_jeko.sh
    
   #Interactive mode
    bash eval.sh
    
   #Score 
    bash score.sh
  </pre></code>
