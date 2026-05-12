import Phone
import requests
import subprocess
import json


def scrape(text, phonedict):
    infinityx_devices = json.loads(text)
    for phone in infinityx_devices:
        codename = phone["name"].split(".")[0]
        support = ["infinity-x"]

        # r = subprocess.check_output(['ls', '-l'])
        # requests.get(phone["download_url"], allow_redirects=True)

        try:
            info = json.loads(r.text)
        except:
            continue

        if codename is None:
            continue
        codename = str(codename).lower()
        if phonedict.get(codename) is None:
            # lazy HACK: ... some  could do this for me
            phonedict[codename] = Phone.Phone(
                "", info["devicemodel"], codename, support
            )
        else:
            phonedict[codename].support.extend(support)
