from googletrans import Translator
translator = Translator()
# res = translator.translate('안녕하세요.')
res = translator.detect('이 문장은 한글로 쓰여졌습니다.')
print(res)