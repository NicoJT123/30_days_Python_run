#day 15 error
#nothing to do just information

#day 16

from datetime import datetime
# now = datetime.now()
# print(now)                      # 2021-07-08 07:34:46.549883
# day = now.day   #  datetime.now().day              # 8
# month = now.month    #  datetime.now().month          # 7
# year = now.year      #  datetime.now().year          # 2021
# hour = now.hour      #  datetime.now().hour          # 7
# minute = now.minute    #  datetime.now().minute         # 38
# second = now.second    #  datetime.now().second
# timestamp = now.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

# from datetime import datetime
# # current date and time
# now = datetime.now()
# t = now.strftime("%H:%M:%S")
# print("time:", t)           # time: 18:21:40
# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("time one:", time_one)        # time one: 06/28/2022, 18:21:40
# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("time two:", time_two)        # time two: 28/06/2022, 18:21:40


# from datetime import date, datetime
# today = date(year=2026, month=7, day=19)
# new_year = date(year=2027, month=1, day=1)
# time_left_for_newyear = new_year - today
# # Time left for new year:  27 days, 0:00:00
# print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  27 days, 0:00:00

# t1 = datetime(year = 2026, month = 7, day = 19, hour = 22, minute = 16, second = 0)
# t2 = datetime(year = 2027, month = 1, day = 1, hour = 0, minute = 0, second = 0)
# diff = t2 - t1
# print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

# from datetime import date, datetime
# before = date(year=1970, month=1, day=1)
# today = date(year=2026, month=7, day=19)
# time_difference = today - before  
# # Time left for new year:  27 days, 0:00:00
# print('the time difference between 1 January 1970 and now: ', time_difference)  # Time left for new year:  27 days, 0:00:00

# from datetime import timedelta
# t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
# t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
# t3 = t1 - t2
# print("t3 =", t3)

# print(datetime.now().day)