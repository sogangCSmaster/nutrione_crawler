from crawler import product_list, keyword_and_price

def main():
    productList = product_list()

    data = productList[0]
    

    k_n_p = keyword_and_price(data)
    
    print(k_n_p)


if __name__ == '__main__':
    main()