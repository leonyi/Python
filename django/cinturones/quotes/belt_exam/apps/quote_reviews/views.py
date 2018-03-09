from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *


# The index function is called when root is visited
def index(request):
    return render(request, 'quote_reviews/index.html')


def set_session(request, user):
    request.session['id'] = user.id
    request.session['user_name'] = user.name
    request.session['logged_in'] = True


def get_quotes(request):
    all_quotes = []
    all_faves = []

    # Gets the list of quotes.
    for q in Quote.objects.all():
        all_quotes.append(q)

    u = User.objects.get(id=request.session['id'])
    for fq in u.liked_quotes.all():
        all_faves.append(fq)

    return all_quotes, all_faves

def dashboard(request):
    # If we are here, we are logged in!
    all_quotes, all_faves = get_quotes(request)

    context = {
        "all_quotes": all_quotes,
        "all_faves": all_faves,
    }

    return render(request, "quote_reviews/initium.html", context)


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


def add_fave(request):
    user = User.objects.get(id=request.session['id'])
    liked_quote = Quote.objects.get(id=request.POST['liked_quote_id'])
    user.liked_quotes.add(liked_quote)

    return redirect('/dashboard')


def remove_fave(request):
    user = User.objects.get(id=request.session['id'])
    liked_quote = Quote.objects.get(id=request.POST['liked_id_to_rm'])
    user.liked_quotes.remove(liked_quote)

    return redirect('/dashboard')


def add_quote(request):
    errors, valid_entry = Quote.objects.validate(request.POST)

    if valid_entry:
        q_content = request.POST['quote_content']
        q_author = request.POST['quote_author']
        posted_by_id = User.objects.get(id=request.session['id'])

        Quote.objects.create(quote_content=q_content, quote_author=q_author, quoted_by=posted_by_id)
    else:
        for error in errors:
            messages.error(request, error['message'], error['message_tag'])

    return redirect('/dashboard')


def show_user(request, id):
    user_quotes = []
    user = User.objects.get(id=id)

    for q in user.posted_quotes.all():
        user_quotes.append(q)

    context = {
        "user_name": user.name,
        "quote_count": len(user.posted_quotes.all()),
        "user_quotes": user_quotes
    }

    # Renders a template that shows information for the user.
    return render(request, "quote_reviews/show_user.html", context)