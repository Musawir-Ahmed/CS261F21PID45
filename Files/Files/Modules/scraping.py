from bs4 import BeautifulSoup
from selenium import webdriver
from Modules import extraFunctions
import time
#
## Gets Links from the query page
#
def getLinks(driver,keyWords):
    driver.get("https://www.youtube.com/results?search_query="+keyWords)
    ###
    ###scrolling  the page
    ###
    extraFunctions.auto_scroll(driver)
    ###
    ###Getting links
    ###
    content = driver.page_source
    soup = BeautifulSoup(content)

    List_href=[]
    for a in soup.findAll('div',attrs={'id':'dismissible'}):
        video_url=a.find('a',attrs={'id':'video-title'})
        if not(video_url==None):
            List_href.append(video_url['href'])
            print(video_url['href'])
    ###
    #### Using Links gathered from a keyword
    ###
    return List_href
#
## Get attributes from a given link
#
def getAtrrib(url,driver):
    driver.get(url)
    driver.execute_script("window.scrollTo(0, 550)")
    time.sleep(5)
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('div',attrs={'class':'style-scope ytd-watch-flexy'}):
        name=a.find('yt-formatted-string', attrs={'class':'style-scope ytd-video-primary-info-renderer'})
        views=a.find('span', attrs={'class':'view-count style-scope ytd-video-view-count-renderer'})
        likes=a.find('yt-formatted-string', attrs={'class':'style-scope ytd-toggle-button-renderer style-text','id':'text'})
        if (name!=None and likes!=None):
            ##
            ##Scrapping
            ##
            date=name.find_next('yt-formatted-string', attrs={'class':'style-scope ytd-video-primary-info-renderer'})
            dislikes=likes.find_next('yt-formatted-string', attrs={'class':'style-scope ytd-toggle-button-renderer style-text','id':'text'})
            channel_name=a.find('yt-formatted-string', attrs={'class':'style-scope ytd-channel-name'})
            suscribers=a.find('yt-formatted-string', attrs={'id':'owner-sub-count'})
            duration=a.find('span', attrs={'class':'ytp-time-duration'})
            no_comments=a.find('yt-formatted-string', attrs={'class':'count-text style-scope ytd-comments-header-renderer'})

            ##
            ##saving in variables
            ##
            Vidname = name.text

            if views!=None:
                Vidviews = views.text
            else:
                Vidviews=0

            if date!=None:
                VidDate = date.text
            else:
                VidDate="Not-Avaialable"

            if likes!=None:
                VidLikes = likes.text
            else:
                VidLikes="Not-Avaialable"


            if dislikes!=None:
                VidDislikes = dislikes.text
            else:
                VidDislikes="Not-Avaialable"
            
            if channel_name!=None:
                ChanName = channel_name.text
            else:
                ChanName="Not-Avaialable"


            if suscribers!=None:
                Subs = suscribers.text
            else:
                Subs="Not-Avaialable"

            if duration != None:
                VidDuration = duration.text
            else:
                VidDuration = 0

            if no_comments != None:
                NumCom = no_comments.text
            else:
                NumCom = 0
            ##
            ##creating list
            ##
            DataList = [url,Vidname,ChanName,Subs,Vidviews,VidDate,VidDuration,VidLikes,VidDislikes,NumCom]
            break
    return DataList
#
## Scrapes Completely
#
def scrape(keyWords,driver,path):
    index = 0 
    for i in range(len(keyWords)):
        driver.get("https://www.youtube.com/results?search_query="+keyWords[i])
        ###
        ###scrolling  the page
        ###
        extraFunctions.auto_scroll(driver)
        ###
        ###Getting links
        ###
        content = driver.page_source
        soup = BeautifulSoup(content)

        List_href=getLinks(driver,keyWords[i])
        print("NUMBER OF LINKS",len(List_href))
        for link in List_href:     
            DataList=getAtrrib("https://www.youtube.com/"+link,driver)
            if(DataList!=None):
                extraFunctions.append_data(DataList,path)
                print(DataList)
