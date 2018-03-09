from flask import Flask, render_template, url_for


app = Flask(__name__)

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

    def __str__(self):
        return '{self.firstname} {self.lastname}'.format(self=self)

    def __repr__(self):
        return '{self.firstname} {self.lastname}'.format(self=self)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title="Title passed from view to template",
                           text=["first","second list element from view to template", "third"], user=User("Yanet", "Leon"))

@app.route('/add')
def add():
    return render_template('add.html')
if __name__ == '__main__':
    app.run(debug=True)