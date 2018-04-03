from datetime import date
from datetime import time
from datetime import datetime
import time

class Stop_Watch():

    def __init__(self):
        pass

    def main_menu(self):

        print("Welcome to the humble stop watch..enter \n"
               "\n"
              "Press 1 to start the humble stop watch \n"
              "Once started...press any 'Ctrl+C' to stop the humble stop and display lapsed time")
        choice = input(">.....")
        return int(choice)

    def calculate_time_diff(self):

        choice1 = self.main_menu()

        if choice1 == 1:
                try:
                    start_time = datetime.now()
                    while True:

                        print(datetime.now())
                        time.sleep(1)
                except KeyboardInterrupt:
                    time_lapsed = (datetime.now() - start_time)
                    print('Time elapsed (hh:mm:ss.ms) {}'.format(time_lapsed))
        else:
            self.calculate_time_diff()

my_watch = Stop_Watch()
my_watch.calculate_time_diff()
