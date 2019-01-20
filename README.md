HackedEd-Avengers-2019
Our goal is to create proof of concept application that will empower users to become more financially fit with their day to day transactions.
The application should be able to take a picture of a receipt and extract vital information from it, which will be stored on a database.
The application will also allow you to select a category for the purchase. This can help the user plan fiscally by showing the user how much they are spending, and on what they are spending, over a time period.
This data can then be analyzed, and recommendations will be given to the individual based off his/her spending habits.


RECEIPT PARSER:
-can determine the date for vast majority of samples via importing regex and utilizing .findall()
-the name of store where the purchase was made can be generally determined by reading the first line of the text
-total amount spent can be found by taking the first few integers after "TOTAL:", the decimal point, as well as the 2 integers after
-
