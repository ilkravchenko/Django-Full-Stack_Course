from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_view) # domain.com/my_first_app
    
    
    # path('', views.index, name='index'), #my_first_apps --> PROJECT urls.py
    # path('<int:num_page>', views.num_page_view, name='num_page_view'),
    # path('<str:page>/', views.news_page, name='news_page'),
    # path('<int:num1>/<int:num2>', views.add_nums, name='add_nums')
]