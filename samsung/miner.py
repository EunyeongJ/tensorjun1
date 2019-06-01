from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import re # 정규표현식. 콘다 내장 라이브러리

class Samsung:
    def __init__(self):
        pass

    @staticmethod
    def read_file():
        okt = Okt()
        okt.pos("삼성전자 글로벌센터 전자사업부", stem=True) # 어간만 추출하겠다.
        filename = 'data/kr-Report_2018.txt'
        with open(filename, 'r', encoding='UTF-8') as f:
            texts = f.read()
        return texts

    @staticmethod
    def extract_hangeul(texts):
        temp = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힇]+') # 한글만
        temp = tokenizer.sub('', temp) # 한글빼고 다 지워라
        return temp

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize()
        print(tokens[:7])