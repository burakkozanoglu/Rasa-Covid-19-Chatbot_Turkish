import requests
from bs4 import BeautifulSoup

url="https://www.worldometers.info/coronavirus/country/turkey/"
def Corona_cases(url):
    page = requests.get(url)
    print(page)

    soup = BeautifulSoup(page.text, "html.parser")
    pew = soup.findAll(['span'])


    data=[]
    for subs in pew:
        if subs.get_text()!='[source]':
            if subs.get_text()!='':
                if '\n'not in subs.get_text():
                    if not any([i in subs.get_text() for i in [i for i in 'aeiou']]):
                        data.append(subs.get_text())
    return data

if __name__=="__main__":
    out=Corona_cases(url)
    print(out)