from flask import Flask
from flask import  render_template

app = Flask(__name__)


bullets = [
    "箇条書き1",
    "箇条書き2",
    "箇条書き3",
]

# "/" : http://127.0.0.1:5000/ のところに表示
@app.route("/japan/<city>")
def hello(city):
    return render_template("hello.html", city=city, bullets=bullets)  # hello.htmlで使用するcity=URLの引数のcity
