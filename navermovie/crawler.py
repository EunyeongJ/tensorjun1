from selenium import webdriver
from time import sleep # 뻗기 전에 시간을 주는 것
from bs4 import BeautifulSoup

class NaverMovie:
    def __init__(self, url):
        driver = webdriver.Chrome('chromedriver')
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup)