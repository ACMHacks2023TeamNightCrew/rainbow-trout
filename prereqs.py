import requests
from bs4 import BeautifulSoup

base = "https://catalog.ucsc.edu"
res = requests.get(base + "/en/current/general-catalog/courses/")

# First get the list of all the course departments
body = BeautifulSoup(res.content, "html.parser").body
depts = body.find("ul", {"class": "sc-child-item-links"}).find_all("a", href=True)
links = [(dept.text.split(" ")[0].split("-")[0], (base + dept["href"]) + "/") for dept in depts]

courseNames = list()
description = dict()
for dept, link in links:
    deptRes = requests.get(link)
    soup = BeautifulSoup(deptRes.text, "html.parser").body
    # Get the list of courses in unformatted form
    courses = soup.find("div", {"id": "main"}).find("div", {"class": "courselist"})
    print(courses)
    for course in courses:
        print("-" * 65)
        print(course)
        if course.strip().startswith(dept):
            courseNames.append(description)
            description = {"course": " ".join(course.strip()[0:2])}
    print(courseNames)
    break