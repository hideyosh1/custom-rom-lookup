import Phone
import re
from bs4 import BeautifulSoup


def scrape(text, phonedict):
    soup = BeautifulSoup(text, "html.parser")
    iode_phones = soup.find("tbody")
    if iode_phones is None:
        raise Exception("Failed to find iodeos phones")
    for phone in iode_phones.find_all("tr"):
        # vendor not on the page fo rsome reason
        # print(phone)
        support = ["iodéos"]

        items = phone.find_all("td")

        if not items:
            continue

        brand = items[0].text
        name_and_codename = phone.find("a")
        if not name_and_codename:
            continue

        codename = re.findall(r"\([\w\d]+\)$", name_and_codename.text)[0]
        name = name_and_codename.text.replace(codename, "").strip()
        codename = codename.strip("(").strip(")")

        if codename is None:
            continue
        codename = str(codename).lower()
        if phonedict.get(codename) is None:
            phonedict[codename] = Phone.Phone(brand, name, codename, support)
        else:
            phonedict[codename].support.extend(support)
