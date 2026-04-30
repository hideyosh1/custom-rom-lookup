import json
import Phone


def scrape(text, phonedict):
    elixir_devices = json.loads(text)
    for vendor in elixir_devices:
        vendor_name = vendor["deviceCategory"]
        for phone in vendor["deviceDetails"]:
            codename = phone["codeName"]
            support = ["project-elixir"]
            name = phone["deviceName"]

            if phone["deviceStatus"] == "discontinued":
                support = ["project-elixir-discontinued"]

            if codename is None:
                continue
            codename = str(codename).lower()
            if phonedict.get(codename) is None:
                phonedict[codename] = Phone.Phone(vendor_name, name, codename, support)
            else:
                phonedict[codename].support.extend(support)
