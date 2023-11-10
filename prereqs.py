import requests
from bs4 import BeautifulSoup

base = "https://catalog.ucsc.edu"
res = requests.get(base + "/en/current/general-catalog/courses/")

body = BeautifulSoup(res.content, "html.parser").body
depts = body.find("ul", {"class": "sc-child-item-links"}).find_all("a", href=True)
links = [(dept.text.split(" ")[0].split("-")[0], (base + dept["href"]) + "/") for dept in depts]

# TODO
for dept, link in links:
    print(link)
    deptRes = requests.get(link, headers=headers)
    deptBody = BeautifulSoup(deptRes.content, "html.parser").body
    mainBody = body.find("div", {"id": "main"})
    print(mainBody)
    break