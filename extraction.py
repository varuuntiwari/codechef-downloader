def getHeaders(solved):
    tmp, i = [], 0
    for text in solved.find_all('strong'):
        tmp.append(text.get_text())

    print("Sections available to download:")
    for heading in tmp:
        print(f"{(i+1)}. {heading[0:-1]}")
        i+=1
    return tmp

def getSolutions(solved, section):
    tmp = []
    print(solved)
    return tmp