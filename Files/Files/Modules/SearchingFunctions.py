import sys
sys.path.insert(1, 'Files\Files')
from Modules.DataClass import DataList
from Modules import  searchingAlgo

columns = []
def clearcolumns():
    global columns
    columns = []

def AddtoExpression(keyword, columntext, Expression_label):
    found = False
    for i in range(len(columns)):
        if columns[i] == columntext:
            found = True
    if found == False:

        Expression_label.setText(Expression_label.text() + " " + keyword)
        columns.append(columntext)

    if found == True:
        print("This Column has been added already")


def SearchExpression(expression, mainref,algo):
    key = expression.split()
    occurList = searchingAlgo.linear_search(DataList.All,key,columns)
    mainref.searchresult(occurList,algo)
