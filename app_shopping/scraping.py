import requests
from bs4 import BeautifulSoup

class a():
    def sea(goods):
        url = 'https://www.amazon.co.jp/s?k={}'.format(goods)
        # print(url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        #soup_divs = soup.find_all('div', attrs={'data-component-type': 's-search-result'})
        soup_divs = soup.select('sg-col-4-of-12')

        #soup_div = soup_divs[0]
        # soup_result = []
        # print(soup_divs)
        # for soup_div in soup_divs:
        #     print("c")
        #     soup_div_span = soup_div.find_all('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})
        #     print(soup_div_span)
        #     soup_result.append(soup_div_span)
        return soup_divs