import requests
from bs4 import BeautifulSoup
import json
import csv

product_page = ["197"] # 남성 352
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

            headers = {'User-Agent':'Chrome/87.0.4280.88'}
            url = "https://elleswimwear.co.kr/product/list.html?cate_no=" + page + "&page=" + str(pageno)
            response = requests.get(url, headers=headers)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            item_tit = soup.find_all('div', {'class': 'description'})
            
            for tag in item_tit:
                for tag_name in tag('span'):
                    tag_name = tag_name.get_text()
                    if "F" in tag_name:
                        name.append(tag_name)
                    elif "원" in tag_name:
                        price.append(tag_name)
        
        except Exception as e:
            print(e)
        
        pageno = pageno + 1

        if pageno == 3:
            break

with open('elleactive_crawling.csv', 'a', newline='', encoding='utf-8-sig') as w: 
    wr = csv.writer(w) 
    i = 0
    for i in range(len(name)):
        wr.writerow([name[i], '', url_product[i], '새 상품', price[i], '재고 있음', image[i]])

