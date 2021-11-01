from Modules import scraping
from selenium import webdriver 
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import time

def Scrap_link_title(SearchTitle_Url,MainTable,ammount):
    Ammount=ammount.text()
    if(type(Ammount)== "<class 'int'>" or Ammount==""):
        options = webdriver.ChromeOptions()
        options.add_extension('Files/Files/Extensions/Adblock for Youtube™.crx')
        driver = webdriver.Chrome(executable_path='Files/Files/chromedriver_win32/chromedriver.exe', options=options)
        text=SearchTitle_Url.text()
        SearchTitle_Url.setText("")
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        data=scraping.getAtrrib(text,driver)
        rowCount=MainTable.rowCount()
        rowCount=rowCount-100
        MainTable.setItem(rowCount,0,QTableWidgetItem(data[1]))
        MainTable.setItem(rowCount,1,QTableWidgetItem(data[4]))
        MainTable.setItem(rowCount,2,QTableWidgetItem(data[7]))
        MainTable.setItem(rowCount,3,QTableWidgetItem(data[8]))
        MainTable.setItem(rowCount,4,QTableWidgetItem(data[9]))
        MainTable.setItem(rowCount,5,QTableWidgetItem(data[3]))
        MainTable.setItem(rowCount,6,QTableWidgetItem(data[2]))
        MainTable.setItem(rowCount,7,QTableWidgetItem(data[5]))
        MainTable.setItem(rowCount,8,QTableWidgetItem(data[6]))
        MainTable.insertRow(rowCount+1)
        driver.quit()
    else:
        _translate = QtCore.QCoreApplication.translate
        ammount.setPlaceholderText(_translate("MainWindow", " InValid Ammount"))
