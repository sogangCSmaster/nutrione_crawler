nutrioneGMC = 'https://nutrione.co.kr/st/gmc_product.php'
memberPriceXpath = '/html/body/div[3]/div/div/div[1]/div[2]/form/div/div/div[2]/dl[2]/dd/strong/strong/text()'

# ['id', 'title', 'description', 'link', 'image_link', 'availability', 'price', 'brand', 'condition', 'memberPrice', 'contextualKeywords']
fieldsToFeedFormatter = {
    'id': 'ID',
    'title': 'Item title',
    'link': 'Final URL',
    'image_link': 'Image URL',
    'price': 'price',
    'memberPrice': 'sale_price',
    'contextualKeywords': 'Contextual keywords'
}