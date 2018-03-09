from django.shortcuts import render, HttpResponse, redirect
import datetime

# The index function is called when root is visited
def index(request):
    date_now = datetime.datetime.now()
    print date_now.strftime('%b %d %Y, %H:%M %p')

    context = {
        "current_time": date_now.strftime('%b %d %Y, %H:%M %p'),
    }
    return render(request, 'time_display/index.html', context)

