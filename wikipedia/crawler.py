from bs4 import BeautifulSoup
import requests # static에 전역으로 정의되어 있음

class Wiki:
    def __init__(self, url):
        base_url = url
        con = requests.get(base_url)
        soup = BeautifulSoup(con.content, 'html.parser')
        # print(soup)

        infoTable = soup.find('table', {'class':'wikitable sortable'}) # name과 class가 생략 가능하다. name='tables', attr=({'':''})
        result = []
        for a in infoTable.find_all('tr'):
            infolist = []
            for b in a.find_all('td'):
                info = b.get_text()
                infolist.append(info)
            result.append(infolist)
        print(result)
