import time

# def send_emails():
#     for i in range(0, 10000):
#         pass


# start = time.time()
# send_emails()
# end = time.time()

# print('Diff: ', end-start)
from datetime import datetime, timedelta, date

dt = datetime(2022, 12, 3)
print(dt)

print('Now:', datetime.now())
print(datetime.fromtimestamp(time.time()))

dt = datetime.now()
print(f"{dt.year}/{dt.month}")


# * Time deltas:
dt1 = datetime(2022, 1, 1)
dt2 = datetime.now()

duration = dt2-dt1
print(duration)
print('days', duration.days)
print('secs', duration.seconds)
print('total_seconds', duration.total_seconds())


print(datetime)

# *get current date
today = date.today()
print('Current Year:', today.year)
print('Current Month:', today.month)
print('Current Day:', today.day)


# * Convert date to string
print(type(today))
today_str = date.isoformat(today)
print(type(today_str), today_str)
print(today.weekday())
