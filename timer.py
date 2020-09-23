#timer
import time

import winsound

minutes = int(input('How many minutes?'))

seconds = int(input('How many seconds?'))

timer2 = (minutes*60 + seconds)

timer = int(timer2) 

for x in range(timer):
    result = (int(timer - x))
    print(result)
    time.sleep(1)
    
if result == 1:
    print('The timer has been completed')
    winsound.PlaySound("*", winsound.SND_ALIAS) 
else:
    print('an error has occured')
              
def timer():
        pass
    