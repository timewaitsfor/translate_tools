from google_trans_new import google_translator
import pickle

translator = google_translator()

def generate_pickle(path, data):
    with open(path, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def get_zh2en(fn):
    zh2en_dict = {}
    with open(fn, encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i < 15573:
                continue
            # if i % 2000 == 0:
            #     this_translator = google_translator()
            th = line[:-1].split(' ')
            word_index = th[0]
            word_zh_text = th[1]
            word_en_text =  translator.translate(word_zh_text, lang_tgt='en')
            zh2en_dict[word_zh_text] = [word_index, word_en_text.strip()]
            print(word_zh_text, word_en_text)
            # break

    return zh2en_dict

zh2en_dict = get_zh2en("./data/zh2en")
generate_pickle('./data/zh2en_dict.pkl', zh2en_dict)


# translate_text = translator.translate('สวัสดีจีน', lang_tgt='en')
# print(translate_text)