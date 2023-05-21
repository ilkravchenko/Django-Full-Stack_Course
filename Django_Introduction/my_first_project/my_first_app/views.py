from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
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

# redirect from domain.com/my_first_app/0 ---> domain.com/my_first_app/sports
def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    
    try:
        topic = topics_list[num_page]    
        return HttpResponseRedirect(topic)
    except:
        return HttpResponseNotFound('No page for that topic')
    