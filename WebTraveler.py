"""
Web-spider that gets links from an initial website and searches through them recursively.
Beware: while True loop does not stop, until there's a keyboardInterrupt - Press Ctrl + c to stop it.
"""
from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.error import HTTPError
import requests
import re

added_sites = set()
visited_sites = set()
current_run = set()
count = 0

"""
Beautifulsoup html parser with exception handling
"""
def urlError(url):
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


"""
Regex for finding links
"""
def getLinks(url):
    href_link = list()
    bs = urlError(url)
    try:
        for link in bs.find("body").find_all(
                'a', href=re.compile('^http*s://www\..+?\..+')):
            # Parses the sites
            if 'href' in link.attrs:
                href_link.append(link.attrs['href'])
            else:
                print('No link found')
                break
    except AttributeError:
        print("No Link found.\nContinuing.")
    return href_link


"""
Regular expression function which searches through the site-body and writes email-addresses and 7 < character words 
"""
def RegEx(site_body):
    for element in site_body:
        result = element.text
        email = re.findall("(\w+@[a-zA-Z]+?\.[a-zA-Z]{2,6})", result)
        # email regular expression
        email_list = open("CustomEmailList.txt", "a")
        email = set(email)
        print("Emails: ", email)
        for mail in email:
            email_list.write(mail)
            email_list.write("\n")
        results = re.findall("[A-Z][a-z][a-z][a-z][a-z][a-z][a-z][a-z]+", result)
        # 7 < character word with capitalized first letter regular expression
        wordlist = open("CustomWordlist.txt", "a")
        results = set(results)
        print("Word results: ", results)
        for result in results:
            wordlist.write(result)
            wordlist.write("\n")


"""
Main function, searches through the page body, writes emails and words with specified length to a text file
"""
def webTraveler(url):
    soup = urlError(url)
    try:
        body_list = soup.find_all("body")
        RegEx(body_list)
        for link in getLinks(url):
            if link in visited_sites:
                continue
            else:
                current_run.add(link)
        return current_run
    except AttributeError:
        print("No site body has been found.")


added_sites.add(input("Please enter the link you want the traveler to start with:\n"))
while True:
    try:
        print("Round: ", count, "\n")
        print("Those are added sites: ", added_sites)
        count = count + 1
        try:
            for link in added_sites:
                if link in visited_sites:
                    continue
                else:
                    print("Opening: ", link)
                    webTraveler(link)
                    visited_sites.add(link)
            for link in current_run:
                added_sites.add(link)
            if visited_sites == added_sites:
                print("No Links to visit left, exiting")
                quit()
            current_run = set()
        except IndexError:
            print("You have very few lists in your set.\nIs your initial Site not accessible?")
            continue
        except requests.exceptions.ConnectionError:
            continue
    except requests.exceptions.MissingSchema:
        print("Please enter a valid URL")
        quit()
