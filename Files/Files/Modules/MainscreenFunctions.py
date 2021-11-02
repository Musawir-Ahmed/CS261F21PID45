from os import link, path
from Modules import scraping
from Modules import DataClass
from selenium import webdriver 
from PyQt5.QtWidgets import QTableWidgetItem,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import pandas as pd 
import webbrowser

#Declaring Data Object Globally
Data_object=None


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


def Load_Data(File,MainTable):
    if(File!="Select File.."):
        Path="Files\Files\ScrapedData\DataBackup\\"+File
        global Data_object
        data = pd.read_csv(Path) 
        Data_object=DataClass.Data()
        Data_object.Links=data['Link'].tolist()
        Data_object.VideoNames=data['Video Name'].tolist()
        Data_object.ChannelName=data['ChannelName'].tolist()
        Data_object.No_of_Subscribers=data['No. of Subscribers'].tolist()
        Data_object.No_of_Views=data['No. of Views'].tolist()
        Data_object.Date=data['Date'].tolist()
        Data_object.Duration=data['Duration'].tolist()
        Data_object.Likes=data['Likes'].tolist()
        Data_object.Dislikes=data['Dislikes'].tolist()
        Data_object.No_Of_Comments=data['No. Of Comments'].tolist()
        for x in range(0,len(Data_object.VideoNames)):
            rowCount=MainTable.rowCount()
            MainTable.setItem(x,0,QTableWidgetItem(str(Data_object.VideoNames[x])))
            MainTable.setItem(x,1,QTableWidgetItem(str(Data_object.No_of_Views[x])))
            MainTable.setItem(x,2,QTableWidgetItem(str(Data_object.Likes[x])))
            MainTable.setItem(x,3,QTableWidgetItem(str(Data_object.Dislikes[x])))
            MainTable.setItem(x,4,QTableWidgetItem(str(Data_object.No_Of_Comments[x])))
            MainTable.setItem(x,5,QTableWidgetItem(str(Data_object.No_of_Subscribers[x])))
            MainTable.setItem(x,6,QTableWidgetItem(str(Data_object.ChannelName[x])))
            MainTable.setItem(x,7,QTableWidgetItem(str(Data_object.Date[x])))
            MainTable.setItem(x,8,QTableWidgetItem(str(Data_object.Duration[x])))
            MainTable.insertRow(rowCount)


def OpenLink(maintable):
    currentColumn=maintable.currentColumn()
    if(currentColumn==0):
        link=Data_object.Links[maintable.currentRow()]
        if(len(link)<24):
            link="https://www.youtube.com/"+link
            webbrowser.open(link)
        print(link)