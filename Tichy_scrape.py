from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.error import HTTPError
import requests
import re

inner_post_links = []
visited_sites = []


def url_error(url):
    try:
        html = requests.get(url)
    except HTTPError as e:
        print(e)
    except URLError:
        print('The server could not be found!')
    except AttributeError:
        print('Tag was not found')
    else:
        if html is None:
            print('Tag was not found')
        else:
            return BeautifulSoup(html.text, 'html.parser')


def tichy_scrape(url):
    soup = url_error(url)
    title = soup.find("h1", {"class": "entry-title"}).text
    body_list = soup.find_all("div", {"class": "pf-content"})
    better_title = title.replace("\n", "")
    print("Title: {}".format(better_title.rstrip()))
    for element in body_list:
        better_element = str(element.text).replace("\n", "")
        better_element = better_element.replace(". ", ".\n")
        print(better_element)
    for link in soup.find_all("div", {"class": "rty-inner-post-title"}):
        inner_post_links.append(link)
    actual_link = re.findall("href=\"(https*://www\..+\..+/)\"", str(inner_post_links))
    for better_link in actual_link:
        print("Opening", better_link)
        if better_link in visited_sites or better_link == \
                "https://www.tichyseinblick.de/tichys-einblick/tichys-einblick-so-kommt-das-gedruckte-magazin-zu-ihnen/":
            continue
        else:
            visited_sites.append(better_link)
            tichy_scrape(better_link)
    return visited_sites


print(tichy_scrape('https://www.tichyseinblick.de/meinungen/zahlen-zu-asyl-zuwanderung-und-arbeitslosengeld-deutschland-im-hamsterrad/'))

