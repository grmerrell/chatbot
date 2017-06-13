#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup
import re

# open('poemHunterPoems.txt', 'w').close()

#The number of requests you want to send to poemhunter.com
maxRange = int(sys.argv[1])
#List to cross-check authors/titles that have already been added to poems.txt
authorsTitles = [[]]
#Keeps track of # of poems found
poemCount = 0

#Loop through random-poems, adding them to the poem list if they haven't already been added before
for x in range(0,maxRange):

    #set page equal to the current poem's url
    page = requests.get("https://members.poemhunter.com/members/random-poem/")

    #Create an instance of the BeautifulSoup class
    soup = BeautifulSoup(page.content, 'html.parser')

    #Isolate the poem
    poem = soup.select(".poem p")
    poet = soup.select(".poet")
    title = soup.select("h2")

    #Various cleanup actions, lazily written
    poemSpaced = str(poem[0]).replace("<br/>", "\n")
    poemSpaced = str(poemSpaced).replace("<p>\r\n\t\t\t\t\t\t", "")
    poemSpaced = str(poemSpaced).replace("</p>", "")
    poemSpaced = re.sub('<strong>|(?<!\S)\d(?!\S)|(?<!\S)\d\.(?!\S)|\*|(:---).*(---:)|(Translated).*\n?|(?m)^(Part).*\n?|(?m)^(Literal Translation).*\n?|(?m)^(CL).*\n?|(II|IV|V|X|LI|LX).*\n?|(?m)^(\.).*\n?|(?m)^(<p>|<i>).*\n?|(?m)^(\(Florence).*\n?|(?m)^(Copyright).*\n?|(?m)^(Anonymous submission).*\n?|(?m)^(©).*\n?|(?m)^(- -).*\n?|^ *[0-9][0-9 ]*$', '', str(poemSpaced))


    #Check to see if poem has already been added, if not add it to poemHunterPoems.txt
    if authorsTitles.count(poet[0].get_text() + " " + title[0].get_text()) < 1:
        poemCount += 1
        print("Transcribing poem: #" + str(poemCount))
        authorsTitles.append(poet[0].get_text() + " " + title[0].get_text())
        with open('poemHunterPoems.txt', 'a') as f:
            f.write(poemSpaced + "\n")
    else:
        print("Duplicate poem. Trying next poem.")
