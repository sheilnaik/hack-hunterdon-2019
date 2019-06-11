import requests
from bs4 import BeautifulSoup
import time


def scrapLink():
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

    link = input('Please Input an amazon link:')

    raw_html = requests.get(link, headers=headers)

    html = BeautifulSoup(raw_html.text,'html.parser') 

    print(html.text)

    #For some reason beautiful soup would not find all the tags so here we are
    temp = str(html)[100000:10000000]

    #Find the tag that has the title in it
    indexOfLine = temp.find("id=\"bylineInfo\"")

    #Parse to right where the name will be
    while temp[indexOfLine] != '>':
        indexOfLine+=1

    indexOfLine+=1

    #Print out the name from the HTML tag
    while temp[indexOfLine] != '<':
        print(temp[indexOfLine],end='')
        indexOfLine+=1

    #add a new line for spacing
    print()




#,{'role':'listitem'}

    

#    html.find('div',{"id":"a-page"})
#    html.find ('div',{"id":"dp-container"})
#    html.find('div',{"id":"p13n-m-desktop-dp-sims_session-similarities-sims-feature-3"})
#    html.find('div',{"class":"a-section similarities-widget sims-carousel-holder"})
#    html.find('div',{"id":"desktop-dp-sims_session-similarities-sims-feature"})
    




    #    temp = str(i[1])
    #    for j in temp.split("\""):
    #        if(isContent == 1):
    #            for k in j.split(","):
    #                print(k)
    #            break
    #        if(j.endswith("content=")):
    #            isContent = 1



scrapLink()

