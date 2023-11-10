from flask import *
PROJECT_NAME = "Slug Counselor"

app = Flask(__name__, static_url_path="", static_folder="static", template_folder="templates")

@app.route("/form")
def form():
    return render_template("form.html", PROJECT_NAME=PROJECT_NAME)

@app.route("/")
def root():
    return render_template("index.html", PROJECT_NAME=PROJECT_NAME)

if __name__ == "__main__":
    app.run(port=5000)