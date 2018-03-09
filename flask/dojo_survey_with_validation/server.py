from flask import Flask, flash, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "Th!s1sSup3Rsecr37"

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    if request.method == "POST":
        valid = True
        name = request.form['name']
        comment = request.form['commentinput']
        survey = request.form.to_dict()
        print survey

        if len(name) < 1 or len(comment) < 1:
            flash("Name an or comment cannot be empty!".format(name, comment))
            valid = False
        elif len(request.form['commentinput']) > 120:
            flash("Intput field cannot be longer than 120 characters!")
            valid = False

        if valid == True:
            return render_template("survey.html", survey=survey)
        else:
            return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)