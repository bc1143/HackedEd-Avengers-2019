from yelpapi import YelpAPI

city = "Edmonton"
yelp_api = YelpAPI("BkeVvBepP5xWd8hfOi_Pud4wx3d1NWAx7XV_oopCygqKDNuJyE1MBr5TqGhNlBf1KM-cVcz05YsyTGkAkeVq73yTbwbER51fVxc9Qq4vGBhwtCQkjZvPP9LBkvNDXHYx")
op = yelp_api.search_query(term="The Bay", location=city, sort_by='rating', limit = 5)
title2=''
print(op)
title1=op['businesses'][0]['categories'][0]['title']
try:
    title2=op['businesses'][0]['categories'][1]['title']
except IndexError:
    pass
print(title1, title2)