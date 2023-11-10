from flask import *
PROJECT_NAME = "Slug Counselor"
BASEURL = "http://localhost:5000/"

app = Flask(__name__, static_url_path="", static_folder="static", template_folder="templates")

@app.route("/form")
def form():
    return render_template("form.html", PROJECT_NAME=PROJECT_NAME, BASEURL=BASEURL)

@app.route("/")
def root():
    return render_template("index.html", PROJECT_NAME=PROJECT_NAME, BASEURL=BASEURL)

if __name__ == "__main__":
    app.run(port=5000, debug=True)