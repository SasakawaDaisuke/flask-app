from flask import Flask

app = Flask(__name__)

html = """
<h1>サンプルHTML</h1>
<ul>
    <li>箇条書き1</li>
    <li>箇条書き2</li>
    <li>箇条書き3</li>
</ul>
"""


# "/":root のところに表示される
@app.route("/")
def hello_world():
    return html
