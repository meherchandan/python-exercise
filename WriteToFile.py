import requests
from bs4 import BeautifulSoup

def writetofile():
    base_url = 'http://www.nytimes.com'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text,"html.parser")
    content = ""
    for story_heading in soup.find_all(class_="story-heading"): 
        if story_heading.a: 
            content = content + "\n" + story_heading.a.text.replace("\n", " ").strip()
            print(story_heading.a.text.replace("\n", " ").strip())
        else: 
            content = content + "\n" + story_heading.contents[0].strip()
            print(story_heading.contents[0].strip())
    open_file = open("../myoutputdata.txt","w")
    print(content)
    open_file.write(str(content))
    open_file.close()


if(__name__ == "__main__"):
    writetofile()