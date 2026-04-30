import json
import Phone


def scrape(text, phonedict):
    derp_devices = json.loads(text)
    for phone in derp_devices["devices"]:
        support = ["derpfest"]

        codename = phone["codename"]
        if codename is None:
            continue
        codename = str(codename).lower()
        if phonedict.get(codename) is None:
            phonedict[codename] = Phone.Phone(
                "", phone["displayName"], codename, support
            )
        else:
            phonedict[codename].support.extend(support)
