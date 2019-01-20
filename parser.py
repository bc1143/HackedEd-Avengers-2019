'''
can only detect the first instance of the date in the form mm/dd/yyyy OR dd February yyyy OR dd Feb yyyy
'''

import re
def numbered_dates_find(target_string):
    matches = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})', target_string)
    return matches[0][0]
