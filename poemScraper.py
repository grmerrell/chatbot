#poems.com only archives the last 365 poems. The links to the poem count up from an arbitrary number and aren't represented by a date

import requests
from bs4 import BeautifulSoup
import re

page = requests.get("http://poems.com/")
homepage = BeautifulSoup(page.content, 'html.parser')

#find the href to the daily poem
dailyPoemLink = homepage.select("#daily_content strong a")[0].get("href")

#take the last 5 digits from the link and set them equal to num
num = int(re.compile('\d{5}').findall(dailyPoemLink)[0])

#loop through the last 364 days' worth of poems
# for date in range(num-363, num):
for date in range(num-363, num):
    #set page equal to the current poem's url
    page = requests.get("http://poems.com/poem.php?date=" + str(date))

    #Create an instance of the BeautifulSoup class
    soup = BeautifulSoup(page.content, 'html.parser')

    #Isolate the poem
    poem = soup.select("#poem p")

    ##Isolate individual stanzas
    # stanza = soup.select("#poem p br")

    #write the poem to a separate text file
    for x in range(0, len(poem)-1):
        #ignore bolded text, single digits, single digits with periods behind them and asterisks
        # TODO refine. Still ignores certain single digits (e.g., if they're next to certain html tags)
        if re.search('<strong>|(?<!\S)\d(?!\S)|(?<!\S)\d\.(?!\S)|\*', str(poem[x]))==None:
            # print(poem[x])
            with open('poems.txt', 'a') as f:
                f.write(poem[x].get_text().encode("utf-8") + "\n")
