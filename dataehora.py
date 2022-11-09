import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
print('o ano e', year)
print(date)
print(currentDateTime)
