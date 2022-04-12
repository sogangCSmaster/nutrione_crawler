from crawler import product_data, keyword_and_price
from helper import fieldsToFeedFormatter
from multiprocessing import Pool
import csv

def get_dataToInsert(data):
    product = data['product']
    fields = data['fields']
    fullData = keyword_and_price(product)
    dataToInsert = []
    for field in fields:
        if field in fieldsToFeedFormatter:
            dataToInsert.append(fullData[field])
 
    print(dataToInsert)
    return dataToInsert

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
    
    """
    No multi processing
    """
    # for product in productList:
    #     try:
    #         fullData = keyword_and_price(product)
    #         dataToInsert = []
    #         for field in fields:
    #             if field in fieldsToFeedFormatter:
    #                 print(fullData[field])
    #                 dataToInsert.append(fullData[field])
            
    #         fullDatasToInsert.append(dataToInsert)
    #     except:
    #         pass

    
    """
    multiprocessing
    """
    p = Pool(12)
    multiThreadingProcessList = []
    for product in productList:
        # check for deadlocks
        if 'link' in product:
            multiThreadingProcessList.append({'product': product, 'fields': fields})
    
    # start multiprocess
    fullDatasToInsert = p.map(get_dataToInsert, multiThreadingProcessList)

    # githubtest

    wr.writerows(fullDatasToInsert)


if __name__ == '__main__':
    main()