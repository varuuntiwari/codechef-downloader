import requests
from bs4 import BeautifulSoup
import re
from extraction import getHeaders, getSolutions

# Variables for use
user = input('Enter user: ')
ROOT = "https://www.codechef.com/"
URL = ROOT+"users/"+user

page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')

try:
    solved_section = soup.find(class_='problems-solved')
    numSolutions = re.findall('\((\d+)\)', solved_section.find('h5').get_text())[0]
except:
    print("User not found or script has broke, try again..")
    exit(-1)

print(numSolutions,"fully solved solutions are available")
sections = getHeaders(solved_section)

try:
    choice = int(input(": "))
except:
    print("Enter from choices given above!! Aborting..")
    exit(-1)

solutions, i = getSolutions(solved_section, (choice-1)), 0
print("The following code names are solved by the user:")
for link in solutions:
    print(re.findall(f'/([\w\d]+),{user}', link)[0], end=' ')
    i+=1
    if i%10 == 0:
        print()