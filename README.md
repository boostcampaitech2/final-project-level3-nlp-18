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
  4. Input files 
  5. Make JIT folder and input your data

   <pre><code>
   #BPE segments for training
    python bpe_segment.py --jit jit --vocab_size 4000
    
   #Fairseq prepro
    python prepro.py --src ko --tgt je --vocab_size 4000
    python prepro.py --src je --tgt ko --vocab_size 4000
    
   #Training
    bash train_koje.sh
    bash train_jeko.sh
    
   #Interactive mode (User가 input을 넣으면 output이 나오는 화면)
    bash interactive.sh
    
   #Generate (Src 문장을 넣으면 모델을 돌려 Tgt 문장에 대한 해석된 문장을 만들어준다)(--result란을 지운다면 텍스트파일은 만들어지지 않지만 score가 계산이 된다)
    bash generate_koje.sh
    bash generate_jeko.sh
    
   #post-process.py : 만들어진 문장 텍스트에 Detokenized된 문장만을 평문으로 바꿔준 텍스트 파일을 만들어준다
   python post-process.py --vocab_size 4000 --lang1 external --lang2 je

   #backtranslation.py : 만들어진 문장 텍스트를 je.train을 열어 끝에다 기록한다.
   python backtranslation.py --vocab_size 4000 --lang1 external --lang2 je
   
   #Whole.py : 입력을 넣으면 학습한 모델과 data를 이용해 출력하는 파일
  </pre></code>
