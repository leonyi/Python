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

def get_users_pokes(request):
    all_users = User.objects.all().exclude(id=request.session['id'])

    all_poker_pokes = Poke.objects.all().values_list('poker_id', flat=True).distinct()
    user_poke_count = Poke.objects.all().filter(poked=request.session['id'])
    user_poker_list = Poke.objects.filter(poked=request.session['id'])

    pokers_and_counts = dict()
    seen = []
    for obj in user_poker_list:
        if obj.poker.name not in seen:
            seen.append(obj.poker.name)
            pokers_and_counts[obj.poker.name] = 1
        else:
            pokers_and_counts[obj.poker.name] += 1

    print "Pokers and counts: {}".format(pokers_and_counts)



    return all_users, user_poke_count, pokers_and_counts, all_poker_pokes

def dashboard(request):
    # If we are here, we are logged in!
    all_users, user_poke_count, user_poker_list, all_poker_pokes = get_users_pokes(request)

    context = {
        "users_list": all_users,
        "user_poke_count": user_poke_count,
        "user_poker_list": user_poker_list,
        "all_poker_pokes": all_poker_pokes
    }

    return render(request, "belt_app/initium.html", context)

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
    user = User.objects.get(id=id)

    context = {
        "user_name": user.name,
        "user_birthday": user.birth_date,
        "user_email": user.email
    }

    # Renders a template that shows information for the user.
    return render(request, "belt_app/show_user.html", context)

def add_poke(request):
    # Get instace of users.
    poker = User.objects.get(id=request.session['id'])
    poked_user = User.objects.get(id=request.POST['user_id_to_poke'])

    print "in add_poke poker: {} and poked: {}".format(poker, poked_user)

    # Create an instance of poke to populate
    poke = Poke()
    poke.poker = poker
    poke.poked = poked_user
    poke.save()

    return redirect('/dashboard')