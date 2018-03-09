from django.shortcuts import render, HttpResponse, redirect

# The index function is called when root is visited
def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    if request.method == "POST":
        request.session['user_name'] = request.POST['name']
        request.session['geo_location'] = request.POST['geo_location']
        request.session['prog_lang'] = request.POST['prog_language']
        request.session['comment'] = request.POST['comment_input']

    return redirect("survey/result")

def result(request):
    return render(request, 'surveys/survey.html')
