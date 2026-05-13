import requests
import jsonpickle
import subprocess

import bliss
import calyx
import derpfest
import e
import elixir
import graphene
import infinity_x
import iode
import lineage

phonedict = {}

r = requests.get("https://wiki.lineageos.org/devices/")
lineage.scrape(r.text, phonedict)

r = requests.get("https://iode.tech/iodeos-official-supported-devices/")
iode.scrape(r.text, phonedict)
#

r = subprocess.check_output(
    [
        "gh",
        "api",
        "https://api.github.com/repos/ProjectInfinity-X/official_devices/contents/devices?ref=master",
    ]
)
infinity_x.scrape(r, phonedict)

r = requests.get("https://projectelixiros.com/assets/json/download.json")
elixir.scrape(r.text, phonedict)

r = requests.get("https://doc.e.foundation/devices")
e.scrape(r.text, phonedict)

r = requests.get("https://derpfest.org/devices-index.json")
derpfest.scrape(r.text, phonedict)

r = requests.get(
    "https://downloads.blissroms.org/api/v1/blissroms/devices?include_latest_build=true&channel=stable&sort=brand&dir=asc"
)
bliss.scrape(r.text, phonedict)

r = requests.get("http://calyxos.org/install/")
calyx.scrape(r.text, phonedict)

r = requests.get("https://grapheneos.org/releases")
graphene.scrape(r.text, phonedict)


print(jsonpickle.encode(phonedict))


# for codename, phone in phonedict.items():
#     print(phone)
#


# lineageos
