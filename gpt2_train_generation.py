from typing import Dict, List
import torch
from transformers import GPT2LMHeadModel
from transformers import (
    BartConfig,
    BartForConditionalGeneration,
    PreTrainedTokenizerFast,
)
import pandas as pd
import numpy as np

tot = "/opt/Final_project/tot_train.csv"
text = pd.read_csv(tot, usecols= ['표준어'])

ls = []
df = pd.DataFrame()
model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')
for i in range(1, np.shape(text)[0]) : 
    str_text = text.iloc[i,0]
    input_ids = tokenizer.encode(str_text)
    gen_ids = model.generate(torch.tensor([input_ids]),
                                        max_length = 128,
                                        repetition_penalty =2.0,
                                        pad_token_id = tokenizer.pad_token_id,
                                        eos_token_id = tokenizer.eos_token_id,
                                        bos_token_id = tokenizer.bos_token_id,
                                        use_cahce = True,
                                        top_k = 5,
                                        top_p = 0.95
                                        )
    #generateds = tokenizer.decode(gen_ids[0,:].tolist())

    for i, gen_id in enumerate(gen_ids) : 
        print("{} : {}".format(i, tokenizer.decode(gen_id.tolist(), skip_special_tokens=True)))
        ls.append(tokenizer.decode(gen_id.tolist()))

df = pd.DataFrame(ls)
df.to_csv("gen_tot_train.csv", index=False, encoding="utf-8-sig")