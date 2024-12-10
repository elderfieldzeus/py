import datetime

x = datetime.datetime.strptime("12 5 2003", "%d %m %Y")
y = datetime.datetime.strptime("12 5 2004", "%d %m %Y")

print((y - x).days)