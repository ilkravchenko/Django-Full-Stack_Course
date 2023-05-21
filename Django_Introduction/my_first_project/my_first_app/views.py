from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

articles = {
    'sports' : 'Sports Page',
    'finance' : 'Finance Page',
    'politics' : 'Politics Page',
}

def index(request):
    return HttpResponse("Hello world!")

def news_page(request, page):
    try:
        result = articles[page]
        return HttpResponse(result)
    except:
        result = 'No page for that topic'
        # return HttpResponseNotFound(result)
        raise Http404("404 GENERIC ERROR")

def add_nums(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(f'{result}')