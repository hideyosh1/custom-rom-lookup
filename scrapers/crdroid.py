import Phone
from bs4 import BeautifulSoup


def scrape(text, phonedict):
    soup = BeautifulSoup(text, "html.parser")

    for phone in soup.find_all("div", {"class": "card border-secondary shadow"}):
        # vendor not on the page fo rsome reason
        # print(phone)
        support = ["cr-droid"]

        codename = phone.find("h5")
        if codename is None:
            continue

        codename = codename.text

        codename = str(codename).lower()

        name = phone.find("h5", {"class": "devicename"})
        if name is None:
            continue

        if phonedict.get(codename) is None:
            phonedict[codename] = Phone.Phone("", name.text, codename, support)
        else:
            phonedict[codename].support.extend(support)
        # too lazy to do vendor support rn
        # if codename is not None and phonedict.get(codename) is None:
        #     codename = str(codename).lower()
        #     phonedict[codename] = Phone("", name.text, codename, support)
        # else:
        #     phonedict[codename].support.extend(support)
