from flask import *
import catalog_api
import filter
import asyncio

TEAM_NAME = "Team Night Crew"
PROJECT_NAME = "Slug Counselor"
BASEURL = "/"

app = Flask(__name__, static_url_path="", static_folder="static", template_folder="templates")

@app.route("/about-us")
async def aboutUs():
    return render_template("about-us.html", TEAM_NAME=TEAM_NAME, PROJECT_NAME=PROJECT_NAME, BASEURL=BASEURL)

@app.route("/results", methods=["POST"])
async def results():
    taken = []
    cantake = await filter.courses("Computer Science B.S.", taken)
    # cantake = ["CSE 30", "CSE 12", "MATH 19A", "LIT 81I", "CSE 3", "CRWN 1", "HIST 4", "WRIT 1", "SPAN 1", "PSYC 1", "PHIL 22", "AM 10"]
    from random import choice
    schedules = []
    while len(schedules) < 3:
        schedule = []
        while len(schedule) < 3:
            selection = choice(cantake)
            if not selection in schedule:
                schedule.append(selection)
        if schedule.sort not in schedules:
            schedules.append(schedule)
    return render_template("results.html", TEAM_NAME=TEAM_NAME, PROJECT_NAME=PROJECT_NAME, BASEURL=BASEURL, schedules=schedules)

@app.route("/courseList", methods=["GET", "POST"])
async def courseList():
    import json
    courseList = json.loads(open("static/majorLists/Computer Science B.S..json", "r").read())
    return render_template("courseList.html", TEAM_NAME=TEAM_NAME, PROJECT_NAME=PROJECT_NAME, BASEURL=BASEURL, majors="Computer Science B.S.", courses=courseList)

@app.route("/form")
async def form():
    return render_template("form.html", TEAM_NAME=TEAM_NAME, PROJECT_NAME=PROJECT_NAME, BASEURL=BASEURL, majors=catalog_api.MAJORS.keys())

@app.route("/")
async def root():
    return render_template("index.html", TEAM_NAME=TEAM_NAME, PROJECT_NAME=PROJECT_NAME, BASEURL=BASEURL)

@app.route("/api/course/<course>")
async def get_course_info(course):
    return catalog_api.get_course_info(course)

if __name__ == "__main__":
    app.run(port=5000, debug=True)