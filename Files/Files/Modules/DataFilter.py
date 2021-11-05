from time import daylight
import datetime,time
import datetime,time
from datetime import date

def SuscriberFilter(passed_suscriber):
    if(passed_suscriber!="Subscribers"):
        passed_suscriber=passed_suscriber[:-11]
        passed_suscriber=passed_suscriber.replace(" ", "")
        try:
            Multiplier=passed_suscriber[-1]
            if(len(passed_suscriber)>=2 and (Multiplier=="M" or Multiplier=="K")):
                passed_suscriber=passed_suscriber[:-1]
            else:
                Multiplier=1
        except:
            Multiplier=passed_suscriber        
        if(Multiplier=="M"):
            Multiplier=1000000
        elif(Multiplier=="K"):
            Multiplier=1000
        passed_suscriber=float(passed_suscriber)
        Multiplier=int(Multiplier)
        suscribers=Multiplier*passed_suscriber
        suscribers=int(suscribers)
        return suscribers

def views_filter(passed_views):        
    if(passed_views=="No views"):
        return 0
    elif(passed_views=="1 view"):
        return 1
    elif("watching now" in  passed_views):
        passed_views=passed_views[:-13]
        passed_views=passed_views.replace(",", "")
        return int(passed_views)
    elif(passed_views!="0"):
        passed_views=passed_views[:-6]
        passed_views=passed_views.replace(",", "")
        return int(passed_views)
    return 0

def likes_filter(passed_like):
    if(passed_like!="Like"):
        orig=passed_like
        multiplier=1
        endswith=passed_like[-1]
        if not(endswith.isdigit()):
            views=passed_like[:-1]
            if(endswith=="K"):
                multiplier=1000
            elif(endswith=="M"):
                multiplier=1000000
        else:
            views=orig
        views=float(views)
        views=multiplier*views
        views=int(views)
        return views
    else:
        return 0

def dislikes_filter(passed_like):
    if(passed_like!="Dislike"):
        orig=passed_like
        multiplier=1
        endswith=passed_like[-1]
        if not(endswith.isdigit()):
            views=passed_like[:-1]
            if(endswith=="K"):
                multiplier=1000
            elif(endswith=="M"):
                multiplier=1000000
        else:
            views=orig
        views=float(views)
        views=multiplier*views
        views=int(views)
        return views
    else:
        return 0

def comments_filter(passed_comments):
    passed_comments=passed_comments.replace(" ", "")
    passed_comments=passed_comments.replace("Comments", "")
    passed_comments=passed_comments.replace("Comment", "")
    passed_comments=passed_comments.replace(",", "")
    passed_comments=int(passed_comments)
    return passed_comments

def get_Month_value(month):
    months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    try:
        index=months_list.index(month)+1
        return str(index)
    except:
        return "Not Available"

def get_year_value(year):
    if(len(year)==2):
        year="20"+year
    return year

def date_filter(date):
    orignal=date
    month=None
    day=None
    year=None
    if (date[0].isdigit()):
        index=date.find("-")
        day=date[:index]
        date=date[index+1:]
        index=date.find("-")
        month=get_Month_value(date[:index])
        date=date[index+1:]
        year=get_year_value(date)
    else:
        date=date[-12:]
        index=date.find(" ")
        month=date[:index]
        if(len(month)<3):
            date=date[index+1:]
            index=date.find(" ")
        month=get_Month_value(date[:index])
        date=date[index+1:]
        index=date.find(",")
        day=date[:index]
        date=date[index+2:]
        year=get_year_value(date)

    if not(day.isdigit() and month.isdigit() and year.isdigit()):
        current_time = datetime.datetime.now()
        year=current_time.year
        month=current_time.month 
        day=current_time.day
    year=int(year)
    day=int(day)
    month=int(month)
    return datetime.datetime(year, month, day)