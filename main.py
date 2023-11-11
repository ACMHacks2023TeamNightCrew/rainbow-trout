from flask import *
import catalog_api
import asyncio

TEAM_NAME = "Team Night Crew"
PROJECT_NAME = "Slug Counselor"
BASEURL = "/"

app = Flask(__name__, static_url_path="", static_folder="static", template_folder="templates")

@app.route("/about-us")
async def aboutUs():
    return render_template("about-us.html", TEAM_NAME=TEAM_NAME, PROJECT_NAME=PROJECT_NAME, BASEURL=BASEURL)

# @app.route("/results", methods=["POST"])
# async def results():
#     return render_template("form.html", TEAM_NAME=TEAM_NAME, PROJECT_NAME=PROJECT_NAME, BASEURL=BASEURL)

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