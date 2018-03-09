from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *


# The index function is called when root is visited
def index(request):
    return render(request, 'login_registration/index.html')


def login(request):
    errors, user_valid = User.objects.validate_login(request.POST)

    if user_valid:
       for entry in errors:
        context = {
            "message": entry['message'],
            "message_tag": entry['message_tag']
        }
            # messages.error(request, entry['message'], entry['message_tag'])
        return render(request, "login_registration/initium.html", context)
    else:
        for entry in errors:
            messages.error(request, entry['message'], entry['message_tag'])
            return redirect('/')


def registration(request):
    errors, valid_entry = User.objects.validate_registration(request.POST)

    if valid_entry:
        message = User.objects.new_user(request.POST)
        for entry in message:
            messages.error(request, entry['message'], entry['message_tag'])
        return render(request, "login_registration/initium.html")
    else:
        for entry in errors:
            messages.error(request, entry['message'], entry['message_tag'])
            return redirect('/')


def signout(request):
    request.session.clear()
    return redirect('/')
