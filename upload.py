import requests
import re
import json
import os
import shutil

url = "https://nekoweb.org/api/files/upload"
ls_url = "https://nekoweb.org/api/files/readfolder"
delete_url = "https://nekoweb.org/api/files/delete"

headers = {"Authorization": os.environ["NEKOWEB_API_TOKEN"]}

# , "application/octet-stream")} data = {"pathname": "/test"}

extant = requests.request(
    "GET", ls_url, headers=headers, params={"pathname": "./pepsi.nekoweb.org/"}
)
serverfiles = json.loads(extant.text)
serverset = set()
for key in serverfiles:
    serverset.add(key["name"])
# print(serverfiles)
# print(serverset)
# Assign directory

directory = "./dist/"
shutil.copy2("src/robots.txt", directory)
# shutil.copy2("src/elements.css", directory)


names = set()
upfolds = dict()

# Iterate over files in directory
for path, folders, files in os.walk(directory):
    # Open file
    upfolds[path] = []
    for filename in files:
        upfolds.get(path, []).append(
            ("files", open(os.path.join(path, filename), "rb"))
        )
        names.add(filename)

print(upfolds)

for path in upfolds:
    response = requests.request(
        "POST",
        url,
        headers=headers,
        data={"pathname": "/pepsi.nekoweb.org/" + path.replace("./dist/", "")},
        files=upfolds[path],
    )
    print(response.text)

# Read content of file
# print(f.read())
intersect = names & serverset

exempt_str = ["asset*", "wlog"]
exempt_patterns = []
for pattern in exempt_str:
    exempt_patterns += [re.compile(pattern)]


print(serverset)
print(names)
for file in serverset:
    if file not in intersect:
        exempt = False
        for pattern in exempt_patterns:
            if pattern.match(pattern, file) is not None:
                exempt = True
        if exempt:
            continue
        print(file)
        response = requests.request(
            "POST",
            delete_url,
            data={"pathname": f"/pepsi.nekoweb.org/{file}"},
            headers=headers,
        )
        print(response.text)
