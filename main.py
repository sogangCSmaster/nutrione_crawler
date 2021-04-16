from crawler import product_data, keyword_and_price
from helper import fieldsToFeedFormatter
import csv

def main():
    productData = product_data()
    productList = productData['productList']
    fields = productData['fields']
    
    fields = fields + ['memberPrice', 'contextualKeywords']

    f = open('write.csv','w')
    wr = csv.writer(f)
    fieldsToFeed = []

    for field in fields:
        try:
            fieldsToFeed.append(fieldsToFeedFormatter[field])
        except:
            pass
        
    wr.writerow(fieldsToFeed)

    for product in productList:
        fullData = keyword_and_price(product)
        dataToInsert = []
        for field in fields:
            dataToInsert.append(fullData[field])
        wr.writerow(dataToInsert)


if __name__ == '__main__':
    main()