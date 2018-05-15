#!/usr/bin/env python

import argparse

# pip install validators
import validators
import requests
import re

# pip install bs4
from bs4 import BeautifulSoup
from urllib.parse import *

# Challenge:
#
# Create a command line program that will take an internet domain name (i.e. "jana.com") and print out a list of the
# email addresses that were found on that website only.
#
# Example:
#
# The following is expected output from jana.com and web.mit.edu, but it should also run on other websites. In the
# example of jana.com, the program should not crawl other subdomains (blog.jana.com, technology.jana.com).
#
# # These are expected output from www.jana.com
# > python find_email_addresses.py www.jana.com
# Found these email addresses:
# sales@jana.com
# press@jana.com
# info@jana.com
#
# More information:
#
# You can use any modern programming language you like. We work in Python and Java, so one of those is preferred but
# not required.
# Create a new github repository for this project. The repository should be public but please give it some kind of
# codename that doesn't have the word jana in it. The master branch should be empty, and then create a branch with
# your code in it.
# Push your branch up to github, and create a pull request. Send me the link to the pull request, and I can comment
# directly on it. All our code goes through this code review process, so it's a little glimpse into how we work.
# In your repo, please include a readme that has any instructions we might need to setup and install your solution.
# Your program must work on another computer, so be sure to include any required libraries (using libraries is OK).
# You do not need to check in the source for those libraries. Build scripts and/or a requirements.txt file would
# be preferred.
#
# Hints:
#
# Make sure to find email addresses on any discoverable page of the website, not just the home page.
# Style:
#
# At Jana we follow the Google Style Guides for Python and Java. However, it is not critical for this challenge.

class WebPageCrowler:
    __domainName = ""
    __emails = set()
    __processedLinks = set()
    __isValidDomain = True

    def __init__(self, domain):
        self.__checkDomainName(domain)

    def __checkDomainName(self, newDomainName):
        domain = newDomainName.lower()

        if domain[0:4] == "www.":
            domain = domain.replace("www.", "", 1)

        # print("Domain name to process: ", domain)

        if not validators.domain(domain):
            # print("The domain name is invalid.")
            self.__isValidDomain = False
            return

        self.__domainName = domain

    def setDomainName(self, newDomainName):
        self.__checkDomainName(newDomainName)

    def isValidDomain(self):
        return self.__isValidDomain

    def getDomainName(self):
        return self.__domainName

    # This function returns all web pages from html page.
    # Constrain: web pages should be the same leves as our __domainName
    def getWebLinks(self, htmlResp):
        soup = BeautifulSoup(htmlResp.content, "html.parser")
        links = list()

        for link in soup.find_all('a', href=True):
            # we have a constraint, we consider only one level domain names
            link = link['href'].lower()
            link = self.rebuildURL(link)
            if link in self.__processedLinks:
                continue

            uri = urlparse(link)

            newDomainName = uri.netloc
            if newDomainName[0:4] == "www.":
                newDomainName = newDomainName.replace("www.", "", 1)

            if newDomainName != self.__domainName:
                continue

            links.append(link)
        # end of for

        # for link in links:
        #     print(link)

        return links

    def collectEmails(self):
        # WARNING: there is no guarantee we will find all pages with this domain name
        # because those pages can be dynamically generated or exist without any links to each other.
        # If there is not-linked graph it's hard to find all info. It's not a GOOGLE :)
        # This method will work only with linked pages

        if not self.__isValidDomain:
            print("Provided domain name is not valid. Exit.")
            return self.__emails

        # start from base page
        # possible double visit of this page.
        # TODO: check it later.
        self.processWebPage(self.__domainName)

        return self.__emails

    def extractEmails(self, htmlContent):
        emails = re.findall(r'[\w\.-]+@[\w\.-]+.[\w\.-]+', htmlContent)

        # double check our emails
        for email in emails:
            if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)\
                    and email not in self.__emails:
                self.__emails.add(email)

        # self.__emails = self.__emails.union( set(emails) )

    def rebuildURL(self, url):
        if url.startswith('http://www.'):
            return 'http://' + url[len('http://www.'):]
        if url.startswith('www.'):
            return 'http://' + url[len('www.'):]
        if url.startswith('//www.'):
            return 'http://' + url[len('//www.'):]
        if not url.startswith('http://'):
            return 'http://' + url

        return url

    def processWebPage(self, link):
        resp = None

        link = self.rebuildURL(link)

        # check if we already processed this link
        if link in self.__processedLinks:
            return

        try:
            # get all web pages with the same domain name
            resp = requests.get(link)
        except requests.exceptions.ConnectionError:
            print("Web link '%s' does not exist." % (link))

            # mark as processed
            self.__processedLinks.add(link)
            return
        except Exception as ex:
            print("Could not process '%s'. Exception: '%s'" % (link, str(ex)))
            exit(0)

        # skip the page we cannot read
        if resp.status_code != 200:
            # print("Cannot read html page", link)

            # TODO: possible it's one time error. Try retry later
            # TODO: ...

            self.__processedLinks.add(link)
            return

        # get all emails from this html page
        self.extractEmails(resp.text) # get Unicode text

        # mark as processed
        self.__processedLinks.add(link)

        links = self.getWebLinks(resp)
        for newLink in links:
            self.processWebPage(newLink)
    # end of function

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program will find all emails from provided domain name.')
    parser.add_argument('--domain', required=True)
    options = parser.parse_args()

    crowler = WebPageCrowler(options.domain)
    emails = crowler.collectEmails()
    print("Found these email addresses:")
    for email in emails:
        print(email)
