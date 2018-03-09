from django.shortcuts import render, HttpResponse, redirect
import datetime

# The index function is called when root is visited
def index(request):
    return render(request, 'session_words/index.html')

def add(request):
    date_now = datetime.datetime.now()
    display_string = " - Added on " + date_now.strftime('%H:%M %p, %B %d %Y')
    print display_string

    request.session['display_string'] = display_string

    if request.method == "POST":
        for key, val in request.POST.items():
            print "key: {} val: {}".format(key, val)

            if key == "new_word":
                request.session['word'] = val

            if key == "font_color":
                request.session['color'] = val

            if key == "big_font" and val == "on":
                request.session['big_font'] = "big"
                print  request.session['big_font']

    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]

    return redirect('/')