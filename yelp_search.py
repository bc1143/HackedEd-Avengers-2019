'''
import json
'''
'''
from pyquery import PyQuery as pq
import requests as rq
import xml.etree.ElementTree as ET

place ='blaze+pizza'
location = 'Edmonton'
province = 'AB'
url = "http://www.yelp.com/search?find_desc=" + place + "find_loc=" + location + "+" + province + "+Canada"

yelp = rq.get(url)
doc = pq(yelp.text)
print(doc)

links = doc('li.moredetails a')
print (len(links))
for link in links:
    print (pq(link).attr('href'))

'''
'''
jsonData = json.loads('yelp_dataset.tar')
'''
'''
import responses
from yelp.client import Client

MY_API_KEY = "BkeVvBepP5xWd8hfOi_Pud4wx3d1NWAx7XV_oopCygqKDNuJyE1MBr5TqGhNlBf1KM-cVcz05YsyTGkAkeVq73yTbwbER51fVxc9Qq4vGBhwtCQkjZvPP9LBkvNDXHYx" 
client = Client(MY_API_KEY)


YELP_SAN_FRANCISCO = responses.Response(
    method="GET",
    url="https://api.yelp.com/v3/businesses/yelp-san-francisco",
    #json=read_json_file("business_lookup_yelp_san_francisco.json"),
    #status=200,
)

'''
from yelpapi import YelpAPI
city = "Edmonton"
yelp_api = YelpAPI("BkeVvBepP5xWd8hfOi_Pud4wx3d1NWAx7XV_oopCygqKDNuJyE1MBr5TqGhNlBf1KM-cVcz05YsyTGkAkeVq73yTbwbER51fVxc9Qq4vGBhwtCQkjZvPP9LBkvNDXHYx")
print(yelp_api.search_query(term="McDonalds", location=city, sort_by='rating', limit = 5))

