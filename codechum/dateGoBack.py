import datetime

month1 = input("Input month: ")
day1 = input("Input day: ")
year1 = input("Input year: ")

date = datetime.datetime.strptime("{}-{}-{}".format(month1, day1, year1), "%B-%d-%Y")

goBack = int(input("Days to go back: "))

newDate = date - datetime.timedelta(days=goBack)

print(newDate.strftime("%B %d, %Y"))