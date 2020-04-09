import datetime

now = datetime.date.today()

John = datetime.date(1991, 5, 13)

#Year = now.year - John.year
#YearInDay = Year * 365
#Months = now.month - John.month
#MonthsInDays = (365/12) * Months
#Dayss = YearInDay + MonthsInDays
#print(Dayss)

Years = now.year - John.year
print (Years)

Month = now.month - John.month
print(Month)

Days = (now - John).days
print(Days)
