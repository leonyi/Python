from django.shortcuts import render, HttpResponse, redirect
import random, string


# The index function is called when root is visited
def index(request):
    # if request.method == "POST":
    try:
        request.session['counter'] += 1
    except:
        request.session['counter'] = 1

    string_length = 14
    rand_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(string_length))

    context = {
        "random_string": rand_string,
    }

    return render(request, 'random_word/index.html', context)
