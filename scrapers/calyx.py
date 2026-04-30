import requests
import Phone
from bs4 import BeautifulSoup


def scrape(text, phonedict):
    soup = BeautifulSoup(text, "html.parser")

    for phone in soup.find_all("tr"):
        # vendor not on the page fo rsome reason
        # print(phone)
        support = ["calyxos-discontinued"]

        items = phone.find_all("td")

        if not items:
            continue

        name = phone.find("a")
        if not name:
            continue

        codename = items[1].text

        if codename is None:
            continue
        codename = str(codename).lower()
        if phonedict.get(codename) is None:
            phonedict[codename] = Phone.Phone("", name.text, codename, support)
        else:
            phonedict[codename].support.extend(support)
        # if codename is not None and phonedict.get(codename) is None:
        #     codename = str(codename).lower()
        #     phonedict[codename] = Phone("", name.text, codename, support)
        # else:
        #     phonedict[codename].support.extend(support)
