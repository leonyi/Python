from django.shortcuts import render, HttpResponse, redirect

from models import *

# The index function is called when root is visited
def index(request):
    # Anything done on the django shell can go here!
    # Example:
    # context = {
    #     "blogs" = Blog.objects.all()
    # }
    # return render(request, 'index.html', context )
    #
    # OR
    #
    # return render(request, 'index.html', Blog.objects.all())

    response = "Placeholder to later display all the list of blogs."
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a new blog."
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print "*" * 50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*" * 50
        return redirect("/")
    else:
        return redirect("/")

def show(request, number):
    response = "Placeholder to display blog {}.".format(number)
    return HttpResponse(response)

def edit(request, number):
    response = "Placeholder to edit blog {}.".format(number)
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')

