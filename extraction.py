def getHeaders(solved):
    tmp, i = [], 0
    # Store text of strong tags(section headings)
    for text in solved.find_all('strong'):
        tmp.append(text.get_text())

    # Printing section headings
    print("Sections available to download:")
    for heading in tmp:
        print(f"{(i+1)}. {heading[0:-1]}")
        i+=1
    return tmp

def getSolutions(solved, section):
    tmp = []
    # Extracts all p tags(sections), span tag(code section) then a tags(individual codes)
    solutionLinks = solved.find_all('p')[section].find('span').find_all('a')
    for link in solutionLinks:
        # Store link to user submissions of code
        tmp.append(link.get("href"))
    return tmp