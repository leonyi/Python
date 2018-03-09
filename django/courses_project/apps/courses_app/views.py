from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

# The index function is called when root is visited
def index(request):
    return redirect('/dashboard')

def set_session(request, user):
    request.session['id'] = user.id
    request.session['user_name'] = user.name
    request.session['logged_in'] = True

def dashboard(request):
    # Add logic to render
    context = {
        "courses_list": Course.objects.all()
    }

    return render(request, "courses_app/index.html", context)

def add_course(request):
    notifications = Course.objects.validate(request.POST)
    if notifications:
        for errors in notifications:
            messages.error(request, errors['message'], extra_tags=errors['message_tag'])
            return redirect('/')
    else:
        description = Description()
        description.description_field = request.POST['course_description']
        description.save()

        Course.objects.create(name=request.POST['course_name'], description=description)

    return redirect('/dashboard')

def render_remove_page(request, id):
    return render(request, 'courses_app/show_confirmation.html', {"course": Course.objects.get(id=id)})

def delete_course(request, id):
    course = Course.objects.get(id=id)
    messages.success(request, "Course ({}) Successfully Deleted".format(course.id), "course_deletion")

    course.delete()

    return redirect('/dashboard')

def render_course_comments(request, id):
    return redirect('/dashboard')