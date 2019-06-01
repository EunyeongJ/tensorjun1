# 자연어 처리를 위한 nltk
import nltk
nltk.download('book', quiet=True)
from nltk.book import *

class Emma:
    def __init__(self):
        nltk.corpus.gutenberg.fileids()
        emma_raw = nltk.gutenberg.raw('austen-emma.txt')
        print(emma_raw[:1302])  # 1302 글자까지 출력