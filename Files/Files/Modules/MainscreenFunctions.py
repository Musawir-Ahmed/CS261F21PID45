from os import link, path
from Modules import scraping
from Modules import DataClass
from Modules import extraFunctions
from Modules import sortingAlgo
from selenium import webdriver 
from PyQt5.QtWidgets import QTableWidgetItem,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import pandas as pd 
import webbrowser
import random

#Declaring Data list Object Globally
Data_list_object=None
Data_list_object=DataClass.DataList()
##Declares When The Programs Starts
#Declaring Data Object Globally
Data_Attribute_object=None
##Declares When The Programs Starts
Table=None

def LoadData_Table(MainTable,data):
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

def AppendData_To_List(data):
    Data_list_object.Links.append(data[0])
    Data_list_object.VideoNames.append(data[1])
    Data_list_object.No_of_Views.append(data[4])
    Data_list_object.Likes.append(data[7])
    Data_list_object.Dislikes.append(data[8])
    Data_list_object.No_Of_Comments.append(data[9])
    Data_list_object.No_of_Subscribers.append(data[3])
    Data_list_object.ChannelName.append(data[2])
    Data_list_object.Date.append(data[5])
    Data_list_object.Duration.append(data[6])

def CreatDataObject(Link,videoName,Views,Likes,Dislikes,Comments,Suscribers,ChannelNames,Date,Duration):
    Data_Attribute_object=DataClass.DataAttributes()
    Data_Attribute_object.Links=Link
    Data_Attribute_object.VideoNames=videoName
    Data_Attribute_object.No_of_Views=Views
    Data_Attribute_object.Likes=Likes
    Data_Attribute_object.Dislikes=Dislikes
    Data_Attribute_object.No_Of_Comments=Comments
    Data_Attribute_object.No_of_Subscribers=Suscribers
    Data_Attribute_object.ChannelName=ChannelNames
    Data_Attribute_object.Date=Date
    Data_Attribute_object.Duration==Duration
    Data_list_object.All.append(Data_Attribute_object)

def Scrap_Link(SearchTitle_Url,MainTable):
    options = webdriver.ChromeOptions()
    options.add_extension('Files/Files/Extensions/Adblock for Youtube™.crx')
    driver = webdriver.Chrome(executable_path='Files/Files/chromedriver_win32/chromedriver.exe', options=options)
    text=SearchTitle_Url.text()
    SearchTitle_Url.setText("")
    driver.switch_to.window(driver.window_handles[0])
    data=scraping.getAtrrib(text,driver)
    LoadData_Table(MainTable,data)
    AppendData_To_List(data)
    CreatDataObject(data[0],data[1],data[4],data[7],data[8],data[9],data[3],data[2],data[5],data[6])
    driver.quit()    

def scrapButton_pressed(SearchTitle_Url,MainTable,ammount):
    url_title=SearchTitle_Url.text()
    url_title=url_title    [ 0 : 7 ]
    Ammount=ammount.text()
    if(url_title=="https:/"):
        Scrap_Link(SearchTitle_Url,MainTable)

    elif (Ammount.isdecimal()):
        ScrapTitle(SearchTitle_Url,MainTable,Ammount,ammount)
    
    else:
        ammount.setText("")
        _translate = QtCore.QCoreApplication.translate
        ammount.setPlaceholderText(_translate("MainWindow", " InValid Ammount"))

def ScrapTitle(SearchTitle_Url,MainTable,ammount,AmmounRefrence):
    options = webdriver.ChromeOptions()
    options.add_extension('Files/Files/Extensions/Adblock for Youtube™.crx')
    driver = webdriver.Chrome(executable_path='Files/Files/chromedriver_win32/chromedriver.exe', options=options)
    driver.switch_to.window(driver.window_handles[0])
    link_List=scraping.getLinks(driver,SearchTitle_Url.text())
    print(ammount,len(link_List))
    if(int(ammount)>len(link_List)):
        ammount=len(link_List)
        AmmounRefrence.setText("Max Links ="+str(len(link_List)))
    counter=0
    data=[]
    if(len(link_List)>int(ammount)):
        for x in range(0,int(ammount)):
            if(len(link_List[x])<24):
                link_List[x]="https://www.youtube.com/"+link_List[x]
            print("Link",link_List[x])
            temp=scraping.getAtrrib(link_List[x],driver)
            data.append(temp)
    
    driver.quit()   

    for x in range(0,len(data)):
        LoadData_Table(MainTable,data[x])
        AppendData_To_List(data[x])
        CreatDataObject(data[x][0],data[x][1],data[x][4],data[x][7],data[x][8],data[x][9],data[x][3],data[x][2],data[x][5],data[x][6])
    
    number=random.randint(0,10000000000000)
    extraFunctions.append_data(data,'Files/Files/ScrapedData/UserData-'+str(number)+'.csv')

def Load_Data(File,MainTable):

    global Table

    Table=MainTable
    
    if(File!="Select File.."):
        Path="Files\Files\ScrapedData\\"+File
        global Data_list_object,Data_Attribute_object
        data = pd.read_csv(Path) 
        Data_list_object.Links=data['Link'].tolist()
        Data_list_object.VideoNames=data['Video Name'].tolist()
        Data_list_object.ChannelName=data['ChannelName'].tolist()
        Data_list_object.No_of_Subscribers=data['Subscribers'].tolist()
        Data_list_object.No_of_Views=data['Views'].tolist()
        Data_list_object.Date=data['Date'].tolist()
        Data_list_object.Duration=data['Duration'].tolist()
        Data_list_object.Likes=data['Likes'].tolist()
        Data_list_object.Dislikes=data['Dislikes'].tolist()
        Data_list_object.No_Of_Comments=data['Comments'].tolist()

        #Creating Datat Attributes Object

        for x in range(0,len(Data_list_object.VideoNames)):
            rowCount=MainTable.rowCount()
            #
            Data_Attribute_object=DataClass.DataAttributes()
            Data_Attribute_object.Links=Data_list_object.Links[x]
            Data_Attribute_object.VideoNames=Data_list_object.VideoNames[x]
            Data_Attribute_object.No_of_Views=Data_list_object.No_of_Views[x]
            Data_Attribute_object.Likes=Data_list_object.Likes[x]
            Data_Attribute_object.Dislikes=Data_list_object.Dislikes[x]
            Data_Attribute_object.No_Of_Comments=Data_list_object.No_Of_Comments[x]
            Data_Attribute_object.No_of_Subscribers=Data_list_object.No_of_Subscribers[x]
            Data_Attribute_object.ChannelName=Data_list_object.ChannelName[x]
            Data_Attribute_object.Date=Data_list_object.Date[x]
            Data_Attribute_object.Duration=Data_list_object.Duration[x]
            #Storing Object in List ALL
            Data_list_object.All.append(Data_Attribute_object)
            #
            MainTable.setItem(x,0,QTableWidgetItem(str(Data_list_object.VideoNames[x])))
            MainTable.setItem(x,1,QTableWidgetItem(str(Data_list_object.No_of_Views[x])))
            MainTable.setItem(x,2,QTableWidgetItem(str(Data_list_object.Likes[x])))
            MainTable.setItem(x,3,QTableWidgetItem(str(Data_list_object.Dislikes[x])))
            MainTable.setItem(x,4,QTableWidgetItem(str(Data_list_object.No_Of_Comments[x])))
            MainTable.setItem(x,5,QTableWidgetItem(str(Data_list_object.No_of_Subscribers[x])))
            MainTable.setItem(x,6,QTableWidgetItem(str(Data_list_object.ChannelName[x])))
            MainTable.setItem(x,7,QTableWidgetItem(str(Data_list_object.Date[x])))
            MainTable.setItem(x,8,QTableWidgetItem(str(Data_list_object.Duration[x])))
            MainTable.insertRow(rowCount)
    print(len(Data_list_object.All))

def OpenLink(maintable):
    currentColumn=maintable.currentColumn()
    if(currentColumn==0):
        link=Data_list_object.Links[maintable.currentRow()]
        if(len(link)<24):
            link="https://www.youtube.com/"+link
        webbrowser.open(link)
        print(link)

def Video_name(sorttype,Maintable,comboBox):
    _list=None
    Algorithm=comboBox.currentText()
    if(Algorithm=="Selection Sort"):
        _list=sortingAlgo.selection_sort(Data_list_object.All,sorttype,"VideoNames")
    elif(Algorithm=="Bubble Sort"):
        _list=sortingAlgo.Buble_sort(Data_list_object.All,sorttype,"VideoNames")
    UpdateData_Table(Maintable,_list)


def LoadData_Table_Object(MainTable,data,rowCount):
    MainTable.setItem(rowCount,0,QTableWidgetItem(str(data.VideoNames)))
    MainTable.setItem(rowCount,1,QTableWidgetItem(str(data.No_of_Views)))
    MainTable.setItem(rowCount,2,QTableWidgetItem(str(data.Likes)))
    MainTable.setItem(rowCount,3,QTableWidgetItem(str(data.Dislikes)))
    MainTable.setItem(rowCount,4,QTableWidgetItem(str(data.No_Of_Comments)))
    MainTable.setItem(rowCount,5,QTableWidgetItem(str(data.No_of_Subscribers)))
    MainTable.setItem(rowCount,6,QTableWidgetItem(str(data.ChannelName)))
    MainTable.setItem(rowCount,7,QTableWidgetItem(str(data.Date)))
    MainTable.setItem(rowCount,8,QTableWidgetItem(str(data.Duration)))


def UpdateData_Table(MainTable,Array):
    rowCount=0
    for x in range(0,len(Array)):
        print(Array[x].Duration)
        LoadData_Table_Object(Table,Array[x],x)

