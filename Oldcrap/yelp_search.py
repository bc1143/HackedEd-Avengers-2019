from yelpapi import YelpAPI
def yelpSearch(store, city="Edmonton"):
    yelp_api = YelpAPI("BkeVvBepP5xWd8hfOi_Pud4wx3d1NWAx7XV_oopCygqKDNuJyE1MBr5TqGhNlBf1KM-cVcz05YsyTGkAkeVq73yTbwbER51fVxc9Qq4vGBhwtCQkjZvPP9LBkvNDXHYx")
    op = yelp_api.search_query(term=store, location=city, sort_by='rating', limit = 5)
    title1 = ''
    title2 = ''
    try:
        title1=op['businesses'][0]['categories'][0]['title']
    except IndexError:
        print('Retailer not Recognized')
    try:
        title2=op['businesses'][0]['categories'][1]['title']
    except IndexError:
        pass
    print(title1, title2)


yelpSearch("A&W")