import requests
from bs4 import BeautifulSoup
import json
import csv

product_page = ["003"] # 남성 004 / 여성 003
print(product_page)

code = []
name = []
url_product = []
price = []
image = []

for page in product_page:
    pageno = 1
    while True:
        try:
            print("상품 " + page + " / " + str(pageno) + "페이지 crawling 진행 중")

            url = "https://www.2xu.kr/goods/goods_list.php?page=" + str(pageno) + "&cateCd=" + page
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            item_tit = soup.find_all('div', {'class': 'item_tit_box'})
            
            for tag in item_tit:
                code.append(tag('span')[0].get_text())
                name.append(tag('strong')[0].get_text())
                for url_tag in tag('a'):
                    url_tag = url_tag['href'].replace('..', '')
                    url_tag = "https://www.2xu.kr" + url_tag
                    url_product.append(url_tag)

            item_money = soup.find_all('div', {'class': 'item_money_box'})

            for tag in item_money:
                price_each = tag('span')[0].get_text().strip()
                price_each = price_each.replace('원', ' KRW')
                price_each = price_each.replace(',', '')
                price.append(price_each)
                
            item_photo = soup.find_all('div', {'class': 'item_photo_box'})

            for tag in item_photo:
                for image_tag in tag('a'):
                    for image_source in image_tag('img'):
                        if "http" in image_source['src'] and "main" in image_source['src']:
                            image.append(image_source['src'])
                        elif "http" not in image_source['src'] and "main" in image_source['src']:
                            image_source['src'] = "https://www.2xu.kr" + image_source['src']
                            image.append(image_source['src'])
                        else:
                            pass
            # item_price = soup.find_all('div', {'class': 'item_money_box'})
            # print(item_price('strong'))
                
        except Exception as e:
            print(e)
        
        pageno = pageno + 1

        if pageno == 18:
            break

with open('2XU_crawling.csv', 'a', newline='', encoding='utf-8-sig') as w: 
    wr = csv.writer(w) 
    i = 0
    for i in range(len(name)):
        wr.writerow([code[i], name[i], '', url_product[i], '새 상품', price[i], '재고 있음', image[i]])

