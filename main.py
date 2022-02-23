import requests
from bs4 import BeautifulSoup
import re
from extraction import getHeaders, getSolutions

# Variables for use
user = input('Enter user: ')
ROOT = "https://www.codechef.com/"
USER = ROOT+"users/"+user

page = requests.get(USER)
soup = BeautifulSoup(page.text, 'html.parser')

try:
    solved_section = soup.find(class_='problems-solved')
except:
    print("User not found or script has broke, try again..")
    exit(-1)

numSolutions = re.findall('\((\d+)\)', solved_section.find('h5').get_text())[0]
print(numSolutions,"fully solved solutions are available")

sections = getHeaders(solved_section)

try:
    choice = int(input(": "))
except:
    print("Enter from choices given above!! Aborting..")
    exit(-1)

solutions = getSolutions(solved_section, sections[choice])
