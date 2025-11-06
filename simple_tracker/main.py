from tracker import Tracker
import time

with open('C:\\Users\\Student\\Desktop\\test_github\\config\\config.txt', 'r') as file:
    lines = file.readlines()
    interval_value = int(lines[0].split('=')[-1])

tracker = Tracker()

while True:
   tracker.increment() 
   print(tracker.count)
   tracker.save_to_file()
   time.sleep(interval_value)

    