import Phone
from bs4 import BeautifulSoup


def scrape(text, phonedict):
    soup = BeautifulSoup(text, "html.parser")

    graphene_phones = soup.find("a", attrs={"href": "#devices"})
    if graphene_phones is None:
        raise Exception("Failed to find grapheneos phones")

    graphene_phones = graphene_phones.parent
    if graphene_phones is None:
        raise Exception("Failed to find grapheneos phones")

    graphene_phones = graphene_phones.ul
    if graphene_phones is None:
        raise Exception("Failed to find grapheneos phones")

    for phone in graphene_phones.find_all("a"):
        support = ["grapheneos"]

        codename = phone["href"]
        if codename is None:
            continue
        codename = str(codename).strip("#")

        if codename is None:
            continue
        codename = str(codename).lower()
        if phonedict.get(codename) is None:
            phonedict[codename] = Phone.Phone("google", phone.text, codename, support)
        else:
            phonedict[codename].support.extend(support)
