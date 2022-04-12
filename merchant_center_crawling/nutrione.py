import requests
from bs4 import BeautifulSoup
import json
import csv
result = {}
f = open('nutrione_reviews.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(['URL','별 1개','별 2개','별 3개','별 4개','별 5개'])
# url = "https://www.nutrione.co.kr/ajax/review_board_list.php?bdId=goodsreview&searchField=subject_contents&page="
url = "https://www.nutrione.co.kr/board/view.php?&bdId=goodsreview&sno="
# page = 1
sno = 4765
while True:
    try:
        api = url + str(sno)
        response = requests.get(api)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # view_select_item_info = soup.find('span', {'class': 'view_select_item_info'})
        # em = view_select_item_info.find('em').get_text().strip()
        view_select_item_img = soup.find('span', {'class': 'view_select_item_img'})
        print(view_select_item_img)
        link = view_select_item_img.find('a')['href']
        link = link.replace('..', '')
        rating_star = soup.find('span', {'class': 'rating_star'})
        starspan = rating_star.find('span')['style']
        starspan = starspan.replace('width', '')
        starspan = starspan.replace(':', '')
        starspan = starspan.replace('%', '')
        starspan = starspan.replace(';', '')
        starspan = int(int(starspan)/20)
        print(starspan)
        if link not in result:
            result[link] = [0, 0, 0, 0, 0]
            result[link][starspan-1] += 1
        elif link in result:
            result[link][starspan-1] += 1
    except Exception as e:
        print(e)
    sno = sno - 1
    print(sno)
    if sno == 1:
        break
print(result)
for key in result:
    wr.writerow([key,result[key][0], result[key][1], result[key][2], result[key][3], result[key][4]])
f.close()