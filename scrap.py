import requests
import json
from threading import Thread, Lock
from bs4 import BeautifulSoup
from selenium import webdriver

final = []
lock = Lock()

#edit final array
def editArray(url,name):
    #Mutex lock so threads dont compete when adding
    lock.acquire()
    #Appened to the list
    final.append((url,name))
    #Unlock for more threads
    lock.release()


def scrapLink(link):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

    raw_html = requests.get(link, headers=headers)
    html = BeautifulSoup(raw_html.text,'html.parser')

    #print(html.text)

    #For some reason beautiful soup would not find all the tags so here we are
    temp = str(html)[100000:10000000]

    #Find the tag that has the title in it
    indexOfLine = temp.find("id=\"bylineInfo\"")

    #Parse to right where the name will be
    while temp[indexOfLine] != '>':
        indexOfLine+=1

    indexOfLine+=1
    name = ''

    #Print out the name from the HTML tag
    while temp[indexOfLine] != '<':
        #print(temp[indexOfLine],end='')
        name = name+temp[indexOfLine]
        indexOfLine+=1

    #add findings to the final array
    editArray(link,name)

    #Return the name
    return name


def getRec(link):
    #Load selenium with the chrome driver
    driver = webdriver.Chrome()
    driver.get(link)

    #Get the needed div with an xpath query
    temp = driver.find_element_by_xpath("//*[@class='a-begin a-carousel-container a-carousel-display-swap a-carousel-transition-swap']")

    #Return the library with the list of Amazon IDs for the reccomended items
    return (json.loads(temp.get_attribute("data-a-carousel-options")))["initialSeenAsins"]


listofURLs = getRec('https://www.amazon.com/dp/B07CSG9R72')

#Define thread buffer
threads = []



#For all of the threads initialize then and add them to buffer
for index in range(len(listofURLs)):
    threads.append(Thread(target=scrapLink, args=('https://www.amazon.com/dp/'+listofURLs[index],)))
    threads[index].start()

#Start all the threads and join then
for amazonID in threads:
    amazonID.join()

#print out the final answer
print(final)

