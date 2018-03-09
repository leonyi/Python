from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    if request.method == "POST":
        survey = request.form.to_dict()
        print survey

    return render_template("survey.html", survey=survey)

if __name__ == '__main__':
    app.run(debug=True)