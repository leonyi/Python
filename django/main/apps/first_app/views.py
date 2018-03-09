from django.shortcuts import render, HttpResponse, redirect

# The index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

# This function will be called when test is visited.
def test(request):
    response = "Hello, I am test!"
    return HttpResponse(response)
