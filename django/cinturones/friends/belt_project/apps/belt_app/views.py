from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

# The index function is called when root is visited
def index(request):
    return render(request, 'belt_app/index.html')


def set_session(request, user):
    request.session['id'] = user.id
    request.session['user_name'] = user.name
    request.session['logged_in'] = True

def get_users(request):
    all_users = []
    all_friends = []

    for u in User.objects.all():
        all_users.append(u)

    # Gets all users of a given friend.
    u = User.objects.get(id=request.session['id'])
    for f in [friendship.to_friend for friendship in u.friend_set.all()]:
        all_friends.append(f)

    # Gathers the list of non-friends.
    not_friends = set(all_users) - set(all_friends)

    return not_friends, all_friends


def dashboard(request):
    # If we are here, we are logged in!
    not_friends, all_friends = get_users(request)

    context = {
        "all_non_friends": not_friends,
        "all_friends": all_friends
    }

    return render(request, "belt_app/initium.html", context)

def login(request):
    notifications, user = User.objects.validate_login(request.POST)

    if user:
        set_session(request, user)
        return redirect('/dashboard')
    else:
        for error in notifications:
            messages.error(request, error['message'], error['message_tag'])
            return redirect('/')


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


def show_user_profile(request, id):
    user = User.objects.get(id=id)

    context = {
        "user_name": user.name,
        "user_email": user.email
    }

    # Renders a template that shows information for the user.
    return render(request, "belt_app/show_user.html", context)

def delete_from_friends(request,id):
    friendship_object = dict()
    db_query = "SELECT id FROM belt_app_friendship where from_friend_id={} and to_friend_id={}".format(request.session['id'],id )

    for o in Friendship.objects.raw(db_query):
        friendship_object['friendship_names'] = o
    friendship_object['id'] = o.id
    Friendship.objects.get(id=friendship_object['id']).delete()

    return redirect('/dashboard')

def add_as_friend(request):
    user = User.objects.get(id=request.session['id'])
    new_friend = User.objects.get(id=request.POST['added_friend_id'])
    friendship = Friendship(from_friend=user, to_friend=new_friend)
    friendship.save()

    return redirect('/dashboard')

