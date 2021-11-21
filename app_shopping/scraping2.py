import requests
from bs4 import BeautifulSoup



def sea(goods):
        url = 'https://search.rakuten.co.jp/search/mall/{}'.format(goods)
        # print(url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        items=soup.select('.searchresultitem')
        #print(items)
        
        n=1
        
        data_rakuten = []
        
        for item in items:
            title=item.select_one('.title').text.replace('\n','')
            price=item.select_one('.price').text.replace('\n','').replace(' ','')
            url=item.find('a').get('href')
            
            # print('商品名：{}　価格：{}'.format(title,price))
            # print('-'*30)
            #print(url)
            data_rakuten.append([title, price, url])
            
            if n>10:
                break
            n+=1

        return data_rakuten   