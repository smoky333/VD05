# Создайте свой HTML-шаблон (файл base.html).
# Создайте страницы home.html и about.html, которые будут расширять шаблон и заполнять
# его контентом.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
