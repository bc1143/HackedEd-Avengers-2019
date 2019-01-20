'''
This program can categorically sort the store where the receipt was obtained.
Taking the name of the store, the name is run through a dictionary (d).
If a match is obtained, the category is automatically obtained.
If there is no match, the user is asked to enter the main type of the store (Services/Retail/Marketing)
If an uninterpretable answer is gotten, the user is asked to type again.
Once the main category is recorded, the user is then asked for the sub-section.
Once both are obtained, the data is stored into the dictionary for future reference.

Will either use this program to sort the categories, or Ibrahim's database, he can complete it.

-Han Wang
'''



name='Edo Japan'

d={
    'McDonalds':['Retail','Fast Food'],
    'Burger King':['Retail','Fast Food'],
    'Subway':['Retail','Fast Food'],
    'Save On Foods':['Retail','Grocery Store'],
    'Magnolia Golf':['Services','Golf'],
    'Princess Auto':['Services','Auto']
}

if name in d:
    type=d[name]
else:

    while True:
        ans1 = input('Retail or Marketing or Services?')
        if ans1=='Retail' or ans1=='Marketing' or ans1=='Services':
            print('good answer')
            break

    ans2=input('What is the sub-section?')
    d[name]=[ans1,ans2]
    type=d[name]

print(name,'-',d[name])
