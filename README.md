# Final-project-level3-nlp-18
  final-project-level3-nlp-18 created by GitHub Classroom


## How to use fairseq translation model

### Requirements 
  python >= 3.6  
  NumPy >= 1.11.1    
  Sentencepiece   
  tqdm   
### Practice
  <pre><code>
  git clone https://github.com/pytorch/fairseq.git
  cd fairseq
  pip install --editable ./ 
 </pre></code>
  1. Input files in your fairseq folder
  2. Make JIT folder and input your data 

   <pre><code>
   #BPE segments for training
    python bpe_segment.py --jit jit --vocab_size 4000 --external 'off' 
    
   #Fairseq prepro
    python prepro.py --src je --tgt ko --vocab_size 4000
    python prepro.py --src ko --tgt je --vocab_size 4000   
    
   #Training
    bash train_koje.sh
    bash train_jeko.sh
    
   #Interactive mode (외부 문장에 대한 생성과 입출력에 쓰인다)
    bash interactive.sh
    
   #Score (src 문장을 넣으면 모델을 돌려 tgt 문장에 대한 해석된 문장의 점수를 계산한다)
    bash generate_koje.sh
    bash generate_jeko.sh
   
   ##Backtranslation
    1. Put external data in your directory(fairseq) 
    2. Split external data 
        python practice.py
        
    3. Make dictionary and preprocess  
        python bpe_segment.py --jit jit --vocab_size 4000 --external 'on'
        python prepro.py --src external --tgt je --vocab_size 4000

    4. Generate file 
        bash generate_ex2je.sh (with best_model made by ko-je training)
      
    5. 4에서 만들어진 제주어를 je.train에 붙이고, 외부데이터를 ko.train에 붙입니다
        python make_pararell.py
      
    6. 1~3의 모든 데이터를 이용해 학습
      
    
  
  </pre></code>
