from crawler import product_data, keyword_and_price
from helper import fieldsToFeedFormatter
import csv

def main():
    productData = product_data()
    productList = productData['productList']
    fields = productData['fields']
    
    fields = fields + ['memberPrice', 'contextualKeywords']

    f = open('feed.csv','w', encoding='utf-8-sig')
    wr = csv.writer(f)
    fieldsToFeed = []

    for field in fields:
        try:
            fieldsToFeed.append(fieldsToFeedFormatter[field])
        except:
            pass
        
    wr.writerow(fieldsToFeed)

    fullDatasToInsert = []
    for product in productList:
        fullData = keyword_and_price(product)
        dataToInsert = []
        for field in fields:
            if field in fieldsToFeedFormatter:
                print(fullData[field])
                dataToInsert.append(fullData[field])
        
        fullDatasToInsert.append(dataToInsert)
        break

    wr.writerows(fullDatasToInsert)


if __name__ == '__main__':
    main()