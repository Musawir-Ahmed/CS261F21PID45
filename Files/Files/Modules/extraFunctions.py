import math
import time
from csv import writer

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

######To Append Data In the file
def append_data(DataList,path):
    with open(path, 'a+', newline='',encoding="utf-8") as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(DataList)