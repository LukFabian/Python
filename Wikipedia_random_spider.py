# Webcrawler for wikipedia sites - input a valid wikipedia URL (of an article) and
# it will spider randomly through wikipedia articles
# have fun

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
href_link = list()
# Create a list, which will later be used to store the wikipedia links with the 'href'-attribute
count = 0
# A counter which will be utilised to initialise the ScrapeRandom


def getLinks(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    # Open the url parameter with the beautifulsoup4 html parser
    for link in bs.find('div', {'id':'bodyContent'}).find_all(
            'a', href=re.compile('^(/wiki/)((?!:).)*$')):
        # Parses the wikipedia sites with a regular expression to get the links
        if 'href' in link.attrs:
            href_link.append(link.attrs['href'])
            # Adds every link with the "href"-attribute to the list we created earlier
        else:
            print('No link found')
            break
            # Breaks the for-loop if no link with the "href"-attribute has been found
    return href_link


def ScrapeRandom(new_url):
    if new_url is None:
        # Input for the initial link, to start the spider
        getLinks(input('Please enter a valid URL: '))
        random_link_number = random.randint(0, len(href_link))
        # chooses the new link via a random selection between all href-links
        random_halflink = href_link[random_link_number]
        random_link = 'https://en.wikipedia.org' + random_halflink
        print(random_link)
        return random_link
    else:
        getLinks(new_url)
        # Opens the url we created with this function in the first(and every other) iteration of this function
        # other than that, it is exactly the same code as the "if"
        random_link_number = random.randint(0, len(href_link))
        random_halflink = href_link[random_link_number]
        random_link = 'https://en.wikipedia.org' + random_halflink
        print(random_link)
        return random_link


while True:
    try:
        if count == 0:
            new_link = ScrapeRandom(None)
            # Initialisation of ScrapeRandom with a user-input
        count = count + 1
        ScrapeRandom(new_link)
    except:
        print('No Link found')
        break


