from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

# The index function is called when root is visited
def index(request):
    return render(request, 'login_registration/index.html')


def set_session(request, user):
    request.session['id'] = user.id
    request.session['user_name'] = user.first_name
    request.session['logged_in'] = True

def dashboard(request):
    # If we are here, we are logged in!
    # Add more logic here for things that need to be displayed on the dashboard.
    context = {
        "message": "Welcome! You have successfully registered (or logged in)!",
    }

    return render(request, "login_registration/initium.html", context)

def login(request):
    notifications, user = User.objects.validate_login(request.POST)

    if notifications:
        for error in notifications:
            print "We are in notifications"
            messages.error(request, error['message'], error['message_tag'])
            return redirect('/')
        print "in notifications: {}".format(notifications)
    if user:
        set_session(request, user)
        print "in user: {}".format(user.name)
        return redirect('/dashboard')

def registration(request):
    errors, valid_entry = User.objects.validate_registration(request.POST)

    if valid_entry:
        # The new user records has been validated.  Let's add the user!
        user = User.objects.new_user(request.POST)
        set_session(request, user)
        return redirect('/dashboard')
    else:
        for entry in errors:
            messages.error(request, entry['message'], entry['message_tag'])
            return redirect('/')


def signout(request):
    request.session.clear()
    return redirect('/')


def show_user(request, id):
    user_quotes = []
    user = User.objects.get(id=id)

    context = {
        "user_name": user.first_name,
        "user_birthday": user.birth_date,
        "user_email": user.email
    }

    # Renders a template that shows information for the user.
    return render(request, "login_registration/show_user.html", context)