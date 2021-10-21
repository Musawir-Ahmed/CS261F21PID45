import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from Modules import scraping#importing scraping from module folder
from selenium import webdriver 
import time


options = webdriver.ChromeOptions()

#Add the folowing options If we want to display chorme in maxmized size or the sixe we want to give
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--start-maximized")

#Adding Youtube Add Blocker Extensions
options.add_extension('Files/Files/Extensions/Adblock for Youtube™.crx')

#Use this below if we want to open chrome driver with default account
# options.add_argument("--user-data-dir=C:\\Users\\pc\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(executable_path='C:\\Users\\pc\\Documents\\ChormeDriver\\chromedriver_win32\\chromedriver.exe', options=options)

#To get to the page that is opened due to the instalation of Youtue Add Blocker
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)


#Keyword extracted by using google trend api as this returns random numbers of words trending in the region a day . we stored it in order to get more data

keyWords = ["pewdiepie","asmr","music","markiplier","old town road","billie eilish","pewdiepie vs t series","fortnite","david dobrik","jacksepticeye","joe rogan","james charles","baby shark","bts","dantdm","snl","game grumps","cnn","wwe","lofi","minecraft","shane dawson","fox news","msnbc",

"mrbeast","fgteev","ssundee","t series","gacha life","stephen colbert","flamingo","ariana grande","nightcore","songs","jake paul","lazarbeam","tyt","eminem","taylor" "swift","post" "malone","vanossgaming","memes","jeffree star","trumpstudy music","cardi b","juice wrld","game of thrones","espn",

"car","Qwali","oled","quantum computing","digital marketing","tourist","motor vlogs","fan","unspeakable","john oliver","logan paul","nba youngboy","try not to laugh","blackpink","coryxkenshin","avengers endgame","roblox","andrew yang","dude perfect","last week tonight","peppa pig","mr beast",

"chad wild clay","dunkey","ufc","game theory","nfl","jre","buzzfeed unsolved","popularmmos","drake","borderlands 3","ninja","colbert","sml","tik tok","itsfunneh","undisputed","ben shapiro","seth meyers","rachel maddow","projared","pokemon sword and shield","jeffy","trevor noah","critical role",

"trisha paytas","blippi","gmm","first take","nintendo","queen","sssniperwolf","ryans toy review","tati","funny videos","sis vs bro","jenna marbles","data mining","cpu build","comeidi sketckh","film","space","dark matter","motivational speaker","math","tv","solar","nature","hiking","sale",

"quran translation","naat","students","diffrent counties"]

scraping.scrape(keyWords,driver,'Files/Files/ScrapedData/ScrapData.csv')