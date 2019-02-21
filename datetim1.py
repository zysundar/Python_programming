#from time import*
import datetime
import calendar
import random
'''print(gmtime(0))
time_local=localtime()
print(time_local)
print("year;",time_local[0],time_local.tm_year)
print("Month;",time_local[1],time_local.tm_mon)
print("day",time_local[2],time_local.tm_mday)
print(time())'''
#time_local[0] and time_local.tm_year produce same result.

import time
#from time import time as my_timer
#from time import perf_counter as my_timer  #cal actual time
#from time import monotonic as my_timer 
from time import process_time as my_timer
input("presss enter to start")
wait_time=random.randint(1,10)
time.sleep(wait_time)
start_time=my_timer()
input("press enter to stop")

end_time=my_timer()


print("started at"+time.strftime("%X",time.localtime(start_time)))
print("ended at"+time.strftime("%X",time.localtime(end_time)))
print("your reaction time was {} seconds".format(end_time-start_time))    

