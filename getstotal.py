note="""Main Street Restaurant
6332 Business Drive
Suite 528
Palo Alto California 94301

975~-1628095

Fri 04/07/2017 11:36 AM

Merchant ID: 9hqjxvufdr
Terminal ID: eet ia

Transaction ID: #e6d598ef
Type: CREDIT

PURCHASE
Number : AXXXXXXXXXXXOO4 1
Entry Mode: Swiped

Card Type: DISCOVER

Response: APPROVED
Approval Code: 819543

Sub Total USD} 25.23

ns

USD$ 29.01

Thanks for supporting
local business!

THANK YOU """



to=note.find('Total')

de=note[to:to+15].find('.')
de=de+to

value=note[de:de+3]

value=note[de-1]+value


for x in range(2,6):
    if note[de-x].isdigit():
        value=note[de-x]+value
    else:
        break


print(value)
