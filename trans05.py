from google_trans_new import google_translator
from utils import *
import os
translator = google_translator()

# nohup /root/anaconda3/bin/python -u /root/mo/translate/trans01.py > /root/mo/translate/log/demo121501.log 2>&1 &

file_num = os.path.basename(__file__)[len('trans0'):-len('.py')]
pwd = os.path.abspath('.')

log_f = open(pwd+'/output/trans_res'+file_num+'.txt', 'a+')
this_nt_dict = process_pickle(pwd+'/input/this_nt_dict'+file_num+'.pkl')


def get_zh2en(this_nt_dict):
    zh2en_dict = {}
    for i, (nt_k, nt_v) in enumerate(this_nt_dict.items()):
        word_index = nt_v[0]
        word_zh_text = nt_v[1]
        try:
            word_en_text =  translator.translate(word_zh_text, lang_tgt='en')
        except Exception:
            continue
        zh2en_dict[word_zh_text] = [word_index, word_en_text.strip()]
        print(word_zh_text, word_en_text)
        log_f.writelines(word_zh_text+"\t"+word_en_text+"\n")
        # break

    return zh2en_dict

zh2en_dict = get_zh2en(this_nt_dict)
generate_pickle(pwd+'/output/zh2en_dict'+file_num+'.pkl', zh2en_dict)





