from datetime import datetime, timedelta

#1 task
x = datetime.today() - timedelta(days=5)

print(x)

#2 task
x1 = datetime.today() - timedelta(days=1)
y1 = datetime.today()
z1 = datetime.today() + timedelta(days=1)
print(x1)
print(y1)
print(z1)

#3 task
x2 = datetime.now()
x2 = x2.replace(microsecond=0)
print(x2)

#4 task
date_format = "%Y-%m-%d"

d1 = input("enter d1(YYYY-MM-DD): ")
d2 = input("enter d2(YYYY-MM-DD): ")

try:
    date1 = datetime.strptime(d1, date_format)
    date2 = datetime.strptime(d2, date_format)
except ValueError:
    print("There is a mistake in input")
    exit()

difference_in_seconds = abs(date2 - date1).total_seconds()
print(difference_in_seconds)