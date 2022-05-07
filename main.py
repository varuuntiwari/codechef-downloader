import requests
from bs4 import BeautifulSoup
import re
from extraction import getHeaders, getSolutions
from download import downloadFiles

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
    print("[+] User not found or script has broke, try again..")
    exit(-1)

print(numSolutions,"fully solved solutions are available")
sections = getHeaders(solved_section)

try:
    choice = int(input(": "))
except:
    print("[-] Enter from choices given above!! Aborting..")
    exit(-1)

solutions, i = getSolutions(solved_section, (choice-1)), 0
print("The following code names are solved by the user:")
print('-------------')
for link in solutions:
    print(re.findall(f'/([\w\d]+),{user}', link)[0], end=' ')
    i+=1
    if i%10 == 0:
       print()

print('\n-------------')
print(f'Make sure you have no directory with the name {sections[choice-1][0:-1]}')
confirmation = input(f'Continue with downloading {len(solutions)} solutions?(y/n): ')
if confirmation != 'y':
    print('[-] Aborting operation..')
    exit(-1)

status = downloadFiles(sections[choice-1][0:-1], solutions)
if status != 1:
    exit(-1)
else:
    print('''[+] Downloads successful!\nRemove the solutions from Downloads folder before
downloading other sections with the same name''')