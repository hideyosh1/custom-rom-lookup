"""r = requests.get("https://evolution-x.org/devices", verify=False)
evolution = BeautifulSoup(r.text, "html.parser")
evolution_json = evolution.find("script", attrs={"type": "application/ld+json"})
if evolution_json is None:
    raise Exception("Failed to find evolution phones")
evolution_phones = json.load(evolution_json.text)

for phone in evolution_phones:
    phone = phone["item"]
    codename = phone["codename"]
    support = ["evolution"]
    vendor = phone["brand"]

    if codename is None:
        continue
    codename = str(codename).lower()
    if phonedict.get(codename) is None:
        phonedict[codename] = Phone(vendor, phone["name"], codename, support)
    else:
        phonedict[codename].support.extend(support)"""
