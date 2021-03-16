from google_trans_new import google_translator
from utils import *
import time

translator = google_translator()

# log_f = open('./output/trans_res01.txt', 'a+')

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
def get_zh2en(fn):
    file_num = 1
    with open(fn, encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i % 5000 == 0:
                # this_log_f = open('./output/trans_res'+str(file_num)+'.txt', 'a+')
                try:
                    generate_pickle('./input/this_nt_dict'+str(file_num)+'.pkl', this_nt_dict)
                    file_num += 1
                except Exception:
                    pass
                this_nt_dict = {}

            th = line[:-1].split(' ')
            word_index = th[0]
            word_zh_text = th[1]
            # word_en_text =  translator.translate(word_zh_text, lang_tgt='en')
            this_nt_dict[word_zh_text] = [word_index, word_zh_text]
            # print(word_zh_text, word_en_text)
            # log_f.writelines(word_zh_text+"\t"+word_en_text+"\n")
    generate_pickle('./input/this_nt_dict' + str(file_num) + '.pkl', this_nt_dict)


# get_zh2en("./data/need_translate01")
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# generate_pickle('./data/zh2en_dict01.pkl', zh2en_dict)

num = 0
for i in range(1, 7):
    this_nt_dict = process_pickle('./input/this_nt_dict'+str(i)+'.pkl')
    print(i, len(this_nt_dict))
    num += len(this_nt_dict)

print(num)


