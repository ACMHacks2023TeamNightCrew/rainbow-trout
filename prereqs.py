import requests
from bs4 import BeautifulSoup
import re
import sys

base = "https://catalog.ucsc.edu"
res = requests.get(base + "/en/current/general-catalog/courses/")

def parsereqs(reqs: str):
    "Prerequisite(s): score of 200 or higher on the  mathematics placement examination (MPE), or MATH 2."
    prereqs = list()
    # Math placement
    search = re.search(r"score\s+of\s+(\d+)\s+or\s+higher\s+on\s+the\s+mathematics\s+placement\s+examination\s+", reqs)
    if search != None:
        prereqs.append("MPE " + search.group(1))
    # Search for all the departments
    for dept in depts:
        search = re.search("%s \d+[A-Za-z]?" % dept, reqs)
        if search != None:
            prereqs.append(search.group())
    return prereqs

# First get the list of all the course departments
body = BeautifulSoup(res.content, "html.parser").body
deptElements = body.find("ul", {"class": "sc-child-item-links"}).find_all("a", href=True)
depts = [dept.text.split(" ")[0].split("-")[0] for dept in deptElements]
links = [(dept.text.split(" ")[0].split("-")[0], (base + dept["href"]) + "/") for dept in deptElements]

courseNames = list()
description = dict()
for dept, link in links:
    deptRes = requests.get(link)
    soup = BeautifulSoup(deptRes.text, "html.parser").body
    # Get the list of courses in unformatted form
    courses = soup.find("div", {"id": "main"}).find("div", {"class": "courselist"})
    # print(courses)
    for course in courses:
        lineText = course.text.strip()
        if lineText.startswith(dept):
            if description != dict():
                courseNames.append(description)
            description = {"course": " ".join(lineText.split()[0:2])}
        if lineText.startswith("Requirements"):
            description["reqs"] = lineText
    # break
# print(courseNames[-20])
# We have to parse the requirements
for i in range(len(courseNames)):
    if "reqs" not in courseNames[i]:
        courseNames[i]["prereqs"] = []
        continue
    reqs = courseNames[i]["reqs"]
    while not reqs.startswith("Prerequisite(s)"):
        reqs = reqs[1:]
        if len(reqs) == 0:
            courseNames[i]["prereqs"] = []
            break
    reqs = reqs[17:] # len("Prerequisite(s): ")
    courseNames[i]["prereqs"] = parsereqs(reqs)

# for i in range(len(courseNames)):
#     print(courseNames[i]["course"] + ", ", end="")
#     if "prereqs" in courseNames[i] and courseNames[i]["prereqs"] != 0:
#         print(", ".join(courseNames[i]["prereqs"]))
#     # break

def get(name: str):
    for i in range(len(courseNames)):
        if courseNames[i]["course"] == name:
            return ", ".join(courseNames[i]["prereqs"])
# print(courseNames)