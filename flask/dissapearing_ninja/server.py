from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("allfour.html")

@app.route('/ninja/<color>')
def ninja_color(color):
    to_render = ""
    accepted_colors = ['blue', 'orange', 'red', 'purple']

    if color not in accepted_colors:
        to_render = "notapril.html"
    else:
        to_render = color + "_ninja" + ".html"

    return render_template(to_render)

if __name__ == "__main__":
    app.run(debug=True)