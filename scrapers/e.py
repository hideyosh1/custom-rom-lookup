import Phone
import re
from bs4 import BeautifulSoup


def scrape(text, phonedict):
    soup = BeautifulSoup(text, "html.parser")

    e_phones = soup.find("table")
    if e_phones is None:
        raise Exception("Failed to find /e/ phones")
    for phone in e_phones.find_all("tr"):
        # vendor not on the page fo rsome reason
        # print(phone)
        support = ["/e/os"]

        items = phone.find_all("td")

        if not items:
            continue

        brand = items[0].text
        name = phone.find("a")
        if not name:
            continue

        codename = re.findall(r"\".+\"", items[1].text)[0].strip('"')
        # print(codename)

        if codename is None:
            continue
        codename = str(codename).lower()
        if phonedict.get(codename) is None:
            phonedict[codename] = Phone.Phone(brand, name.text, codename, support)
        else:
            phonedict[codename].support.extend(support)
