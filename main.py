from flask import *
import catalog_api

app = Flask(__name__, static_url_path="", static_folder="static", template_folder="templates")


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/api/course/<course>")
def get_course_info(course):
    return catalog_api.get_course_info(course)


if __name__ == "__main__":
    app.run()