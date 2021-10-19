import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from Modules import scraping#importing scraping from module folder
from selenium import webdriver 
driver = webdriver.Chrome(executable_path=r'C:/Users/Abdul Ahad/Downloads/chromedriver.exe')
keyWords=["dude perfect","ben shapiro","seth meyers","rachel maddow","projared","pokemon sword and shield","jeffy","trevor noah","critical role","trisha paytas","blippi","gmm","first take","nintendo","queen","sssniperwolf","ryans toy review","tati","funny videos","sis vs bro","jenna marbles"]
scraping.scrape(keyWords,driver,'Files/Files/ScrapedData/ScrapData.csv')