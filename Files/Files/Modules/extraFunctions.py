import math
import time

## Function to Scroll down a webpage 
#
def auto_scroll(driver):
    z=1000
    previous_height=-math.inf
    while True:
        z = z+10000
        current_height=driver.execute_script("return document.documentElement.scrollHeight")
        if(current_height==previous_height):
            break
        previous_height=current_height
        scroll="window.scrollTo(0,"+str(z)+")"
        driver.execute_script(scroll)
        time.sleep(3)
        z=z+10000
