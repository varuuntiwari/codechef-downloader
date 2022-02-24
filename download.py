import os
from bs4 import BeautifulSoup
import requests
from re import findall

FOLDER = r'Downloads/'
CORRECTSOL = '?status=FullAC'
ROOT = "https://www.codechef.com/"
CODE = ROOT+'viewplaintext/'

def downloadFiles(section, links):
    status = initFolder(section)
    if status == 0:
        return status
    else:
        print('[+] Folder created')
    for link in links:
        downloadFile(section, link+CORRECTSOL)
    return 1

def initFolder(name):
    try:
        os.makedirs(FOLDER+name)
    except FileExistsError:
        print('Folder already exists')
        return 0
    except FileNotFoundError:
        print('Path cannot be found')
        return 0
    return 1

def downloadFile(section, URL):
    page = requests.get(ROOT+URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    codeLink = soup.find(class_='centered word-break-unset').find('a')
    codeNum = findall('^/viewsolution/(\d+)$', codeLink.get('href'))[0]
    Code = BeautifulSoup(requests.get(CODE+codeNum).text, 'html.parser').find_all('pre')[0].text
    save(section, codeNum, Code)
    print(f'[+] {codeNum}.txt saved')
    
def save(folder, filename, text):
    dir = FOLDER+folder+"/"+filename+".txt"
    if os.path.isfile(dir):
        print(f'{filename} exists already, skipping..')
        return 0
    else:
        f = open(dir, "w+")
        f.write(text)
        f.close()