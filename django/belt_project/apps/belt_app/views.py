from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from collections import Counter

# The index function is called when root is visited
def index(request):
    return render(request, 'belt_app/index.html')


def set_session(request, user):
    request.session['id'] = user.id
    request.session['user_name'] = user.name
    request.session['logged_in'] = True
    request.session['poke_counter'] = 0

def get_users():
    # Modify this function to get more items from the DB if needed.
    users = User.objects.all()

    return users

def dashboard(request):
    # If we are here, we are logged in!
    all_users = get_users()

    context = {
        "users_list": all_users,
    }

    return render(request, "belt_app/initium.html", context)

def login(request):
    notifications, user = User.objects.validate_login(request.POST)

    print "IN login user is is {}".format(user)

    if notifications:
        for error in notifications:
            messages.error(request, error['message'], error['message_tag'])
            return redirect('/')
    if user:
        set_session(request, user)
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
    user = User.objects.get(id=id)

    context = {
        "user_name": user.name,
        "user_birthday": user.birth_date,
        "user_email": user.email
    }

    # Renders a template that shows information for the user.
    return render(request, "belt_app/show_user.html", context)
