from django.urls import path
from .views import HomeView, ThankYou, ContactFormView, TeacherCreateView

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankYou.as_view(), name='thank_you'),
    path('contact/',ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher')
]
