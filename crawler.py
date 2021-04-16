from bs4 import BeautifulSoup
from lxml import html
from helper import nutrioneGMC, memberPriceXpath
import requests
import json

def product_list():
    result = []
    response = requests.get(nutrioneGMC)
    response = response.text
    rows = response.split('\r\n')
    firstRow = rows[0]
    fields = firstRow.split('\t')
    
    for idex, row in enumerate(rows):
        # print(row)
        if idex != 0 :
            temp = {}
            datas = row.split('\t')
            for i in range(0, len(fields)):
                if len(datas) > 1:
                    temp[fields[i]] = datas[i]
            result.append(temp)

    return result

def keyword_and_price(data):
    link = data['link']
    page = requests.get(link)

    tree = html.fromstring(page.content)
    memberPrice = tree.xpath(memberPriceXpath)[0].replace(',', '')

    soup = BeautifulSoup(page.text, 'html.parser')
    meta = soup.find('meta', {'name': 'keywords'})
    contextualKeywords = meta['content']

    data['memberPrice'] = memberPrice
    data['contextualKeywords'] = contextualKeywords

    return data