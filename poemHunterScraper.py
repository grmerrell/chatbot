import requests
from bs4 import BeautifulSoup
# import re

for x in range(0,10000):

    #set page equal to the current poem's url
    page = requests.get("https://members.poemhunter.com/members/random-poem/")

    #Create an instance of the BeautifulSoup class
    soup = BeautifulSoup(page.content, 'html.parser')

    #Isolate the poem
    poem = soup.select(".poem p")

    print("Transcribing poem: #" + str(x))

    poemSpaced = str(poem[0]).replace("<br/>", "\n")
    poemSpaced = str(poemSpaced).replace("<p>\r\n\t\t\t\t\t\t", "")
    poemSpaced = str(poemSpaced).replace("</p>", "")

    with open('poemHunterPoems.txt', 'a') as f:
        f.write(poemSpaced + "\n")
