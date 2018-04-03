from datetime import datetime
from datetime import date
from datetime import timedelta
import sys

print(datetime.today())

today_date = date.today()

print(f"This is a much acceptable date format for me {today_date.day}/{today_date.month}/{today_date.year}")

my_birthday = date(1981, 10, 1)

print(today_date - my_birthday)

print((today_date - my_birthday).microseconds)

if today_date is not my_birthday:
    print(f'I have lived on this planet for {(today_date - my_birthday).days} days!')

my_sleep_duration = timedelta(hours=8)
current_date_time = datetime.today()  # could have also used datetime.now()
print(f'If I dozed off now, I will wake up on {str(current_date_time + my_sleep_duration)}')

def start_watch():
    while True:
        # keep time going
        print(datetime.now())
        sys.stdout.flush()
        #if #stop_watch method is called :
            #set stop time
            #display difference
         #   break


#def stop_watch():

#def time_diff():

start_watch()
