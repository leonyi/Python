from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *

# The index function is called when root is visited
def index(request):
    return render(request, 'user_lab/login.html')

def login(request):
    errors = Admin.objects.validate_admin(request.POST)

    if errors == "valid email":
        messages.error(request, "You are logged in as admin!", extra_tags="valid_admin")
        return redirect("/users")
    else:
        messages.error(request, errors['error'], extra_tags=errors['error_tag'])
        return redirect("/")

def users(request):
    context = {
        "users_list": User.objects.all()
    }

    return render(request, 'user_lab/users.html', context)

def new(request):
    # Renders a form to create a new user.
    return render(request, "user_lab/new_user.html")

def create(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)

        print "In create errors are: {}".format(errors)

        if errors:
            messages.error(request, errors['error'], extra_tags=errors['error_tag'])
            return redirect("/users/new")
        else:
            exists = User.objects.entry_exists(request.POST)

            if not exists:
                created = User.objects.create_entry(request.POST)

                if created:
                    return redirect('/users/{}'.format(created))
                else:
                    messages.error(request, "Internal error: user entry couldn't update.  Contact your administrator!",
                                   extra_tags="internal_error")
            else:
                messages.error(request, "User exists", extra_tags="user_addition")

        return redirect("/users")

def show(request, id):
    # Renders a template that shows information for the user.
    return render(request, "user_lab/show_user.html", {"user": User.objects.get(id=id)})

def edit(request, id):
    return render(request, "user_lab/edit_user.html", {"user": User.objects.get(id=id)})

def update(request, id):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        request.session.id = id

        if errors:
            messages.error(request, errors['error'], extra_tags=errors['error_tag'])
        else:
            updated = User.objects.update_entry(request.POST)

            if updated:
                return redirect('/users/{}'.format(id))
            else:
                messages.error(request, "Internal error: user entry couldn't update.  Contact your administrator!", extra_tags='internal_error' )

        return redirect("/users/{}/edit".format(id))


def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()

    messages.success(request, "User deletion request succeed!", extra_tags="user_deletion")

    return redirect('/users')

def signout(request):
    request.session.clear()

    return redirect('/')

