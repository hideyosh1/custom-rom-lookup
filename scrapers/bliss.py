import requests
import json
import Phone
from bs4 import BeautifulSoup


def scrape(text, phonedict):
    bliss_devices = json.loads(text)
    for phone in bliss_devices["data"]:
        codename = phone["codename"]
        support = ["blissroms"]
        vendor = phone["brand"]

        if codename is None:
            continue
        codename = str(codename).lower()
        if phonedict.get(codename) is None:
            phonedict[codename] = Phone.Phone(vendor, phone["name"], codename, support)
        else:
            phonedict[codename].support.extend(support)
