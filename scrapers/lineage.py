import Phone
from bs4 import BeautifulSoup


def scrape(text, phonedict):
    soup = BeautifulSoup(text, "html.parser")
    for vendor in soup.select("div[data-vendor]"):
        # print(vendor["data-vendor"])
        if vendor["data-vendor"] is None:
            continue
        vendor_name = vendor["data-vendor"]

        for phone in vendor.find_all("div", class_="item"):
            # print(phone)
            codename = phone["data-codename"]
            support = ["lineageos"]

            # print(phone["class"])
            if "discontinued" in phone["class"]:
                support = ["lineageos-discontinued"]

            name = phone.find("span", class_="devicename")

            if not name:
                continue
            # print(code_name.text, device_name.text)
            if codename is None:
                continue
            codename = str(codename).lower()
            if phonedict.get(codename) is None:
                phonedict[codename] = Phone.Phone(
                    vendor_name, name.text, codename, support
                )
            else:
                phonedict[codename].support.extend(support)
