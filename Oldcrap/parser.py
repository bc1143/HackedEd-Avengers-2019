'''
can only detect the first instance of the date in the form mm/dd/yyyy OR dd February yyyy OR dd Feb yyyy
'''

import re
<<<<<<< HEAD
def numbered_dates_find(target_string):
    matches = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})', target_string)
    return matches[0][0]
=======

string = 'I want to apply for leaves from 12/12/2017 to 12/18/2017 I want to apply for leaves from 12 January 2017 to ' \
       '12/18/2017 I want to apply for leaves from 12/12/2017 to 12 Jan 17 '

matches = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})', string)

for match in matches:
    print(match[0])
    break

 '''
 should work for vast majority of receipts
 -Han Wang
 '''
>>>>>>> origin/master
