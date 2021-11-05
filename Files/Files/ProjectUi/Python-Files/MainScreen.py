# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc\Desktop\ProjectUi\UI-Files\MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
#Importing Class OF SearchScreen
from SearchScreen import Ui_SearchFilterWindow
from GraphScreen import Ui_GraphScreen
import _thread
import sys
sys.path.insert(1, 'Files\Files')

from Modules import MainscreenFunctions
from Modules import sortingAlgo

class Ui_MainWindow(object):

    def searchresult(self,occurlist):
        print(occurlist)
        for i in range(len(occurlist)):
            for j in range(9):
                self.MainTable.item(occurlist[i],j).setBackground(QtGui.QColor(255,0,0))
        self.TimeTosearch.setText(str(len(occurlist)))

    #Funtion To Open SearchFilter Screen
    def SearchScreen(self,ui,main):
        Ui_SearchFilterWindow.store_mainrefrence("s",ui)
        Ui_SearchFilterWindow.storemainobjectref("s",main)
        self.window2=QtWidgets.QMainWindow()
        self.ui=Ui_SearchFilterWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()
    #End

    # Function to open Graph plotting Screen
    def GraphPltScreen(self,ui):
        Ui_GraphScreen.store_mainrefrence("s",ui)
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_GraphScreen()
        self.ui.setupUi(self.window3)
        self.window3.show()
    #End


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1207, 688)
        MainWindow.setMaximumSize(QtCore.QSize(1207, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\pc\\Desktop\\ProjectUi\\UI-Files\\../ProjectResource/Graph.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(512, 512))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 341, 31))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setIndent(10)
        self.label.setObjectName("label")
        
        self.SelectAlgorithmcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SelectAlgorithmcomboBox.setGeometry(QtCore.QRect(570, 10, 158, 31))
        self.SelectAlgorithmcomboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SelectAlgorithmcomboBox.setMaxVisibleItems(20)
        self.SelectAlgorithmcomboBox.setObjectName("SelectAlgorithmcomboBox")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")
        self.SelectAlgorithmcomboBox.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1120, 10, 75, 31))
        ####Scrap Button
        ##
        #
        ###Search Url Or Title
        self.SearchTitle_Url = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchTitle_Url.setGeometry(QtCore.QRect(760, 10, 151, 31))
        self.SearchTitle_Url.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SearchTitle_Url.setText("")
        self.SearchTitle_Url.setObjectName("SearchTitle_Url")
        ####
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: MainscreenFunctions.scrapButton_pressed(self.SearchTitle_Url,self.MainTable,self.Amount))#Here
        ####
        self.Amount = QtWidgets.QLineEdit(self.centralwidget)
        self.Amount.setGeometry(QtCore.QRect(960, 10, 141, 31))
        self.Amount.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.Amount.setText("")
        self.Amount.setObjectName("Amount")
        ##
        #
        self.SearchInTable = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchInTable.setGeometry(QtCore.QRect(570, 50, 341, 31))
        self.SearchInTable.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SearchInTable.setText("")
        self.SearchInTable.setClearButtonEnabled(False)
        self.SearchInTable.setObjectName("SearchInTable")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(1120, 50, 75, 31))
        self.SearchButton.setObjectName("SearchButton")
        #Here To Connect to search Filter Window
        ####
        ##
        self.SearchFilterButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchFilterButton.setGeometry(QtCore.QRect(960, 50, 141, 31))
        self.SearchFilterButton.setObjectName("SearchFilterButton")
        print(type(ui))
        self.SearchFilterButton.clicked.connect(lambda:self.SearchScreen(MainWindow,ui))
        self.SearchFilterButton.clicked.connect(MainWindow.hide)
        ####Here to connect to graph plotting window
        ##
        #
        self.PlotGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlotGraphButton.setGeometry(QtCore.QRect(570, 90, 341, 31))
        self.PlotGraphButton.setObjectName("PlotGraphButton")
        self.PlotGraphButton.clicked.connect(lambda:self.GraphPltScreen(MainWindow))
        self.PlotGraphButton.clicked.connect(MainWindow.hide)
        ###
        ##
        #
        ####Adding Button To Load Data
        self.DataLoadcomboBox = QtWidgets.QLineEdit(self.centralwidget)
        self.DataLoadcomboBox.setGeometry(QtCore.QRect(571, 125, 233, 31))
        self.DataLoadcomboBox.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.DataLoadcomboBox.setText("")
        self.DataLoadcomboBox.setObjectName("SearchTitle_Url")


        self.LoadDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadDataButton.setGeometry(QtCore.QRect(810, 125, 100, 31))
        self.LoadDataButton.setObjectName("LoadData")
        self.LoadDataButton.clicked.connect(lambda: MainscreenFunctions.Load_Data(self.DataLoadcomboBox.text(),self.MainTable))
        ####

        self.PlotGraphButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.PlotGraphButton_2.setGeometry(QtCore.QRect(960, 90, 235, 31))
        self.PlotGraphButton_2.setObjectName("PlotGraphButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 321, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\pc\\Desktop\\ProjectUi\\UI-Files\\../../../Downloads/toppng.com-youtube-new-logo-909x204.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 550, 111, 21))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setIndent(10)
        self.label_3.setObjectName("label_3")
        self.CurrentUrl_label = QtWidgets.QLabel(self.centralwidget)
        self.CurrentUrl_label.setGeometry(QtCore.QRect(130, 550, 491, 21))
        self.CurrentUrl_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.CurrentUrl_label.setIndent(10)
        self.CurrentUrl_label.setObjectName("CurrentUrl_label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(673, 550, 121, 16))
        self.label_5.setIndent(10)
        self.label_5.setObjectName("label_5")
        self.ScrapedLinks = QtWidgets.QLabel(self.centralwidget)
        self.ScrapedLinks.setGeometry(QtCore.QRect(791, 550, 141, 16))
        self.ScrapedLinks.setIndent(10)
        self.ScrapedLinks.setObjectName("ScrapedLinks")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(665, 540, 20, 122))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 570, 1191, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(919, 618, 20, 42))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(130, 635, 491, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 635, 111, 21))
        self.label_9.setAutoFillBackground(True)
        self.label_9.setIndent(10)
        self.label_9.setObjectName("label_9")
        self.TimeTookToScrap = QtWidgets.QLabel(self.centralwidget)
        self.TimeTookToScrap.setGeometry(QtCore.QRect(760, 635, 141, 16))
        self.TimeTookToScrap.setIndent(10)
        self.TimeTookToScrap.setObjectName("TimeTookToScrap")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(670, 635, 121, 16))
        self.label_11.setIndent(10)
        self.label_11.setObjectName("label_11")
        self.PausResumebutton = QtWidgets.QPushButton(self.centralwidget)
        self.PausResumebutton.setGeometry(QtCore.QRect(940, 635, 111, 23))
        self.PausResumebutton.setObjectName("PausResumebutton")
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(1070, 635, 111, 23))
        self.StopButton.setObjectName("StopButton")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 650, 1191, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(1, 540, 20, 121))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(1191, 537, 20, 123))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.RemainingLinks = QtWidgets.QLabel(self.centralwidget)
        self.RemainingLinks.setGeometry(QtCore.QRect(1050, 550, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.RemainingLinks.setFont(font)
        self.RemainingLinks.setIndent(10)
        self.RemainingLinks.setObjectName("RemainingLinks")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(930, 550, 121, 16))
        self.label_6.setIndent(10)
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(690, 10, 21, 31))
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setObjectName("label_12")
        self.MainTable = QtWidgets.QTableWidget(self.centralwidget)
        self.MainTable.setGeometry(QtCore.QRect(10, 160, 1191, 381))
        self.MainTable.setAutoFillBackground(False)
        self.MainTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.MainTable.setAutoScrollMargin(10)
        self.MainTable.setAlternatingRowColors(True)
        self.MainTable.setShowGrid(True)
        self.MainTable.setGridStyle(QtCore.Qt.SolidLine)
        self.MainTable.setRowCount(100)
        self.MainTable.setColumnCount(9)
        self.MainTable.setObjectName("MainTable")
        
        item = QtWidgets.QTableWidgetItem()

        self.MainTable.doubleClicked.connect(lambda: MainscreenFunctions.OpenLink(self.MainTable))


        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.MainTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)


        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.MainTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.MainTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.MainTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.MainTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.MainTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.MainTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.MainTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.MainTable.setHorizontalHeaderItem(8, item)

        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setItem(2, 0, item)
        self.MainTable.horizontalHeader().setVisible(True)
        self.MainTable.horizontalHeader().setCascadingSectionResizes(False)
        self.MainTable.horizontalHeader().setDefaultSectionSize(127)
        self.MainTable.horizontalHeader().setHighlightSections(False)
        self.MainTable.horizontalHeader().setMinimumSectionSize(6)
        self.MainTable.horizontalHeader().setSortIndicatorShown(False)
        self.MainTable.verticalHeader().setVisible(True)
        self.MainTable.verticalHeader().setHighlightSections(False)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(10, 609, 1191, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 590, 151, 16))
        self.label_7.setIndent(10)
        self.label_7.setObjectName("label_7")
        self.TimetoSort = QtWidgets.QLabel(self.centralwidget)
        self.TimetoSort.setGeometry(QtCore.QRect(150, 590, 141, 16))
        self.TimetoSort.setIndent(10)
        self.TimetoSort.setObjectName("TimetoSort")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(260, 580, 20, 35))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.SortAlgo = QtWidgets.QLabel(self.centralwidget)
        self.SortAlgo.setGeometry(QtCore.QRect(410, 590, 141, 16))
        self.SortAlgo.setIndent(10)
        self.SortAlgo.setObjectName("SortAlgo")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 590, 151, 16))
        self.label_8.setIndent(10)
        self.label_8.setObjectName("label_8")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(919, 540, 20, 38))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(670, 590, 171, 16))
        self.label_10.setIndent(10)
        self.label_10.setObjectName("label_10")
        self.TimeTosearch = QtWidgets.QLabel(self.centralwidget)
        self.TimeTosearch.setGeometry(QtCore.QRect(830, 590, 141, 16))
        self.TimeTosearch.setIndent(10)
        self.TimeTosearch.setObjectName("TimeTosearch")
        self.SearchingAlgo = QtWidgets.QLabel(self.centralwidget)
        self.SearchingAlgo.setGeometry(QtCore.QRect(1090, 590, 141, 16))
        self.SearchingAlgo.setIndent(10)
        self.SearchingAlgo.setObjectName("SearchingAlgo")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(930, 590, 161, 16))
        self.label_13.setIndent(10)
        self.label_13.setObjectName("label_13")
        self.VideoNam_sortAsecending = QtWidgets.QToolButton(self.centralwidget)
        self.VideoNam_sortAsecending.setGeometry(QtCore.QRect(141, 160, 25, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        ####Video Name
        ##
        #
        self.VideoNam_sortAsecending.setFont(font)
        self.VideoNam_sortAsecending.setObjectName("VideoNam_sortAsecending")
        self.VideoNam_sortAsecending.clicked.connect(lambda: MainscreenFunctions.sort_control("Ascending",self.MainTable,self.SelectAlgorithmcomboBox,"VideoNames",str))

        self.VideoNam_sortdescending = QtWidgets.QToolButton(self.centralwidget)
        self.VideoNam_sortdescending.setGeometry(QtCore.QRect(116, 160, 25, 23))
        self.VideoNam_sortdescending.clicked.connect(lambda: MainscreenFunctions.sort_control("desending",self.MainTable,self.SelectAlgorithmcomboBox,"VideoNames",str))
        #
        ##
        ###


        ###Applying Events On view sort button

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.VideoNam_sortdescending.setFont(font)
        self.VideoNam_sortdescending.setObjectName("VideoNam_sortdescending")
        self.Views_sortAsecending = QtWidgets.QToolButton(self.centralwidget)
        self.Views_sortAsecending.setGeometry(QtCore.QRect(268, 160, 25, 23))
        #Apply funtion sort
        self.Views_sortAsecending.clicked.connect(lambda: MainscreenFunctions.sort_control("Ascending",self.MainTable,self.SelectAlgorithmcomboBox,"No_of_Views",int))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Views_sortAsecending.setFont(font)
        self.Views_sortAsecending.setObjectName("Views_sortAsecending")
        #Apply funtion sort
        self.Views_sortDescending = QtWidgets.QToolButton(self.centralwidget)
        self.Views_sortDescending.setGeometry(QtCore.QRect(243, 160, 25, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Views_sortDescending.clicked.connect(lambda: MainscreenFunctions.sort_control("desending",self.MainTable,self.SelectAlgorithmcomboBox,"No_of_Views",int))

        self.Views_sortDescending.setFont(font)
        self.Views_sortDescending.setObjectName("Views_sortDescending")
        self.Likes_sortAsecending = QtWidgets.QToolButton(self.centralwidget)
        self.Likes_sortAsecending.setGeometry(QtCore.QRect(395, 160, 25, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Likes_sortAsecending.setFont(font)
        self.Likes_sortAsecending.clicked.connect(lambda: MainscreenFunctions.sort_control("Ascending",self.MainTable,self.SelectAlgorithmcomboBox,"Likes",int))

        self.Likes_sortAsecending.setObjectName("Likes_sortAsecending")
        self.Likes_sortDescending = QtWidgets.QToolButton(self.centralwidget)
        self.Likes_sortDescending.setGeometry(QtCore.QRect(370, 160, 25, 23))
        self.Likes_sortDescending.clicked.connect(lambda: MainscreenFunctions.sort_control("desending",self.MainTable,self.SelectAlgorithmcomboBox,"Likes",int))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Likes_sortDescending.setFont(font)
        self.Likes_sortDescending.setObjectName("Likes_sortDescending")


        self.Dislikes_sotrAsecending = QtWidgets.QToolButton(self.centralwidget)
        self.Dislikes_sotrAsecending.setGeometry(QtCore.QRect(521, 160, 25, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Dislikes_sotrAsecending.setFont(font)
        self.Dislikes_sotrAsecending.setObjectName("Dislikes_sotrAsecending")
        self.Dislikes_sortDesecending = QtWidgets.QToolButton(self.centralwidget)
        self.Dislikes_sortDesecending.setGeometry(QtCore.QRect(496, 160, 25, 23))

        self.Dislikes_sotrAsecending.clicked.connect(lambda: MainscreenFunctions.sort_control("Ascending",self.MainTable,self.SelectAlgorithmcomboBox,"Dislikes",int))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.Dislikes_sortDesecending.clicked.connect(lambda: MainscreenFunctions.sort_control("desending",self.MainTable,self.SelectAlgorithmcomboBox,"Dislikes",int))

        self.Dislikes_sortDesecending.setFont(font)
        self.Dislikes_sortDesecending.setObjectName("Dislikes_sortDesecending")
        self.Coments_sotrDescesding_2 = QtWidgets.QToolButton(self.centralwidget)
        self.Coments_sotrDescesding_2.setGeometry(QtCore.QRect(623, 160, 25, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Coments_sotrDescesding_2.setFont(font)
        self.Coments_sotrDescesding_2.setObjectName("Coments_sotrDescesding_2")
        self.Coments_sotrDescesding_2.clicked.connect(lambda: MainscreenFunctions.sort_control("desending",self.MainTable,self.SelectAlgorithmcomboBox,"No_Of_Comments",int))

        self.Coments_sotrAsecending = QtWidgets.QToolButton(self.centralwidget)
        self.Coments_sotrAsecending.setGeometry(QtCore.QRect(648, 160, 25, 23))
        self.Coments_sotrAsecending.clicked.connect(lambda: MainscreenFunctions.sort_control("Ascending",self.MainTable,self.SelectAlgorithmcomboBox,"No_Of_Comments",int))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Coments_sotrAsecending.setFont(font)
        self.Coments_sotrAsecending.setObjectName("Coments_sotrAsecending")
        self.Suscribers_sotrDescesding = QtWidgets.QToolButton(self.centralwidget)
        self.Suscribers_sotrDescesding.setGeometry(QtCore.QRect(749, 160, 25, 23))
        self.Suscribers_sotrDescesding.clicked.connect(lambda: MainscreenFunctions.sort_control("desending",self.MainTable,self.SelectAlgorithmcomboBox,"No_of_Subscribers",int))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Suscribers_sotrDescesding.setFont(font)
        self.Suscribers_sotrDescesding.setObjectName("Suscribers_sotrDescesding")
        self.Suscribers_sortAsecending = QtWidgets.QToolButton(self.centralwidget)
        self.Suscribers_sortAsecending.setGeometry(QtCore.QRect(774, 160, 25, 23))
        self.Suscribers_sortAsecending.clicked.connect(lambda: MainscreenFunctions.sort_control("Ascending",self.MainTable,self.SelectAlgorithmcomboBox,"No_of_Subscribers",int))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Suscribers_sortAsecending.setFont(font)
        self.Suscribers_sortAsecending.setObjectName("Suscribers_sortAsecending")
        self.Channelname_sortDesecending = QtWidgets.QToolButton(self.centralwidget)
        self.Channelname_sortDesecending.setGeometry(QtCore.QRect(875, 160, 25, 23))
        self.Channelname_sortDesecending.clicked.connect(lambda: MainscreenFunctions.sort_control("desending",self.MainTable,self.SelectAlgorithmcomboBox,"ChannelName",str))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Channelname_sortDesecending.setFont(font)
        self.Channelname_sortDesecending.setObjectName("Channelname_sortDesecending")
        self.ChannelName_sortAsecending = QtWidgets.QToolButton(self.centralwidget)
        self.ChannelName_sortAsecending.setGeometry(QtCore.QRect(900, 160, 25, 23))
        self.ChannelName_sortAsecending.clicked.connect(lambda: MainscreenFunctions.sort_control("Ascending",self.MainTable,self.SelectAlgorithmcomboBox,"ChannelName",str))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ChannelName_sortAsecending.setFont(font)
        self.ChannelName_sortAsecending.setObjectName("ChannelName_sortAsecending")
        self.PublishingDate_sortDesecending = QtWidgets.QToolButton(self.centralwidget)
        self.PublishingDate_sortDesecending.setGeometry(QtCore.QRect(1005, 160, 25, 23))
        self.PublishingDate_sortDesecending.clicked.connect(lambda: MainscreenFunctions.sort_control("desending",self.MainTable,self.SelectAlgorithmcomboBox,"Date_Comparison",int))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.PublishingDate_sortDesecending.setFont(font)
        self.PublishingDate_sortDesecending.setObjectName("PublishingDate_sortDesecending")
        self.PublishingDate_sortAsecending = QtWidgets.QToolButton(self.centralwidget)
        self.PublishingDate_sortAsecending.setGeometry(QtCore.QRect(1030, 160, 25, 23))
        self.PublishingDate_sortAsecending.clicked.connect(lambda: MainscreenFunctions.sort_control("Ascending",self.MainTable,self.SelectAlgorithmcomboBox,"Date_Comparison",int))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.PublishingDate_sortAsecending.setFont(font)
        self.PublishingDate_sortAsecending.setObjectName("PublishingDate_sortAsecending")

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)


        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Video Data Analysis"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Path:- Main &gt;</span></p></body></html>"))
        self.SelectAlgorithmcomboBox.setItemText(0, _translate("MainWindow", "Select Algorithms...."))
        self.SelectAlgorithmcomboBox.setItemText(1, _translate("MainWindow", "Merge Sort"))
        self.SelectAlgorithmcomboBox.setItemText(2, _translate("MainWindow", "Bubble Sort"))
        self.SelectAlgorithmcomboBox.setItemText(3, _translate("MainWindow", "Quick Sort"))
        self.SelectAlgorithmcomboBox.setItemText(4, _translate("MainWindow", "Shell Sort"))
        self.SelectAlgorithmcomboBox.setItemText(5, _translate("MainWindow", "Strand Sort"))
        self.SelectAlgorithmcomboBox.setItemText(6, _translate("MainWindow", "Counting Sort"))
        self.SelectAlgorithmcomboBox.setItemText(7, _translate("MainWindow", "Radix Sort"))
        self.SelectAlgorithmcomboBox.setItemText(8, _translate("MainWindow", "Comb Sort"))
        self.SelectAlgorithmcomboBox.setItemText(9, _translate("MainWindow", "Pigeonhole Sort"))
        self.SelectAlgorithmcomboBox.setItemText(10, _translate("MainWindow", "Cycle Sort"))
        self.SelectAlgorithmcomboBox.setItemText(11, _translate("MainWindow", "Cocktail Sort"))
        self.SelectAlgorithmcomboBox.setItemText(12, _translate("MainWindow", "Selection Sort"))
        self.SelectAlgorithmcomboBox.setItemText(13, _translate("MainWindow", "Insertion Sort"))


        # self.DataLoadcomboBox.setItemText(0, _translate("MainWindow", "Select File.."))
        # self.DataLoadcomboBox.setItemText(1, _translate("MainWindow", "ScrapData.csv"))
        # self.DataLoadcomboBox.setItemText(2, _translate("MainWindow", "User.csv"))
        self.DataLoadcomboBox.setPlaceholderText(_translate("MainWindow", " Enter File Name"))


        self.SearchTitle_Url.setPlaceholderText(_translate("MainWindow", " Search Title Or Place Url"))
        self.Amount.setPlaceholderText(_translate("MainWindow", " Enter Ammount"))
        self.pushButton.setText(_translate("MainWindow", "📁 Scrap"))
        self.SearchInTable.setPlaceholderText(_translate("MainWindow", " Search In The Table"))
        self.SearchButton.setText(_translate("MainWindow", "🔎 Search"))
        self.LoadDataButton.setText(_translate("MainWindow", "Load"))
        self.SearchFilterButton.setText(_translate("MainWindow", "🝖 Search Filter"))
        self.PlotGraphButton.setText(_translate("MainWindow", "📈    Plot Graph"))
        self.PlotGraphButton_2.setText(_translate("MainWindow", "📰  Print"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Current Url :- </span></p></body></html>"))
        self.CurrentUrl_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#5500ff;\">https://www.youtube.com/watch?v=4lrojgKYns0&amp;ab_channel=SpinnTV</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Scraped Total:-</span></p></body></html>"))
        self.ScrapedLinks.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">100</span></p><p><span style=\" font-size:10pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Progress       :-</span></p><p><span style=\" font-size:10pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.TimeTookToScrap.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">1.2ms</span></p><p><span style=\" font-size:10pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Time Taken:-</span></p></body></html>"))
        self.PausResumebutton.setText(_translate("MainWindow", "Pause / Resume"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.RemainingLinks.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#0000ff;\">100</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Remaining Links:-</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "🔎"))
        self.MainTable.setSortingEnabled(False)
        item = self.MainTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Video Name"))
        item = self.MainTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Views"))
        item = self.MainTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Likes"))
        item = self.MainTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dislikes"))
        item = self.MainTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "#Comments"))
        item = self.MainTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Suscribers"))
        item = self.MainTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Channel Name"))
        item = self.MainTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Publish Date                                           ."))
        item = self.MainTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Duration"))
        __sortingEnabled = self.MainTable.isSortingEnabled()
        self.MainTable.setSortingEnabled(False)
        self.MainTable.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Time Took To Sort :-</span></p></body></html>"))
        self.TimetoSort.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">3ms<br/></span></p></body></html>"))
        self.SortAlgo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Merge Sort</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Sorting Algorithm  :-</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Total Search Results :-</span></p></body></html>"))
        self.TimeTosearch.setText(_translate("MainWindow", ""))
        self.SearchingAlgo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Binary Search<br/></span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Searching Algorithm :-</span></p></body></html>"))
        self.VideoNam_sortAsecending.setText(_translate("MainWindow", "↓"))
        self.VideoNam_sortdescending.setText(_translate("MainWindow", " ↑ "))
        self.Views_sortAsecending.setText(_translate("MainWindow", "↓"))
        self.Views_sortDescending.setText(_translate("MainWindow", " ↑ "))
        self.Likes_sortAsecending.setText(_translate("MainWindow", "↓"))
        self.Likes_sortDescending.setText(_translate("MainWindow", " ↑ "))
        self.Dislikes_sotrAsecending.setText(_translate("MainWindow", "↓"))
        self.Dislikes_sortDesecending.setText(_translate("MainWindow", " ↑ "))
        self.Coments_sotrDescesding_2.setText(_translate("MainWindow", " ↑ "))
        self.Coments_sotrAsecending.setText(_translate("MainWindow", "↓"))
        self.Suscribers_sotrDescesding.setText(_translate("MainWindow", " ↑ "))
        self.Suscribers_sortAsecending.setText(_translate("MainWindow", "↓"))
        self.Channelname_sortDesecending.setText(_translate("MainWindow", " ↑ "))
        self.ChannelName_sortAsecending.setText(_translate("MainWindow", "↓"))
        self.PublishingDate_sortDesecending.setText(_translate("MainWindow", " ↑ "))
        self.PublishingDate_sortAsecending.setText(_translate("MainWindow", "↓"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #widgets = QtWidgets.QStackedWidget()
    #widgets.addWidget(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())