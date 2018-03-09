from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisisSuperSecret'

# The index route handles the form rendering.
@app.route('/')
def index():
  return render_template("index.html")

# This route handles the form submission.
@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   session['name'] = request.form['name']
   session['email']= request.form['email']
   print request.form

   # Redirects to the route, which will show the the name & email info.
   return redirect('/show')

@app.route("/show")
def show_user():
   # return render_template('user.html', name=session['name'], email=session['email'])
   # We have session data available to the templates directly so we don't have to pass
   # the session info as named parameters!!
   return render_template('user.html')

if __name__ == "__main__":
   app.run(debug=True)

########################################################################################################################
# # This is what is happening behind the scenes:
# 1. We send a browser request to http://127.0.0.1:5000/ & takes us to the form page
# 127.0.0.1 - - [02/Dec/2017 15:35:00] "GET / HTTP/1.1" 200 -
#
# 2. We enter the information on the initial form and click on SUBMIT.  The submit request is of type POST.
# Got Post Info
#
# 3. IN the body of the create user function that received the POST request we use the session data and store it in
# a dictionary:
# ImmutableMultiDict([('name', u'Michelle'), ('email', u'Obama')])
# 127.0.0.1 - - [02/Dec/2017 15:35:21] "POST /users HTTP/1.1" 302 -
#
# 4. The create_user() in server.py sends a redirect to the show_user() function, which takes us to the /show route/html
# 127.0.0.1 - - [02/Dec/2017 15:35:21] "GET /show HTTP/1.1" 200 -
#
# Note: we get these following 404's because we don't have js or css files in the locations defined in the head of
# "user.html"
# file. =)
# 127.0.0.1 - - [02/Dec/2017 15:35:21] "GET /static/css/style_sheet.css HTTP/1.1" 404 -
# 127.0.0.1 - - [02/Dec/2017 15:35:21] "GET /static/js/script.js HTTP/1.1" 404 -
# 127.0.0.1 - - [02/Dec/2017 15:35:21] "GET /static/css/style_sheet.css HTTP/1.1" 404 -
##
########################################################################################################################