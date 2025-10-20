from datetime import datetime, timedelta

given = int(input("How many given: "))

print("Enter {} time reading/s".format(given))

times = [datetime.strptime(input(), "%I:%M %p") for _ in range(given)]

time_to_compare = datetime.strptime(input("Enter time to compare: "), "%I:%M %p")


def getKey(t1):
    key = min(abs(t1 - time_to_compare), abs(time_to_compare - t1), abs(time_to_compare + timedelta(days=1) - t1), abs(t1 + timedelta(days=1) - time_to_compare))
    # print(t1, key)
    return key

s_times = sorted(times, key=getKey)

for t in s_times:
    print(t.strftime("%I:%M %p").lstrip("0"))