from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView

from classroom.forms import ContactForm
from .models import Teacher

# Create your views here.

# def home_view(request):
#     return render(request, 'classroom/home.html')


class HomeView(TemplateView):
    template_name = 'classroom/home.html'
    
    
class ThankYou(TemplateView):
    template_name = 'classroom/thank_you.html'
    
    
class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')
    
    
class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('first_name').all()
    
    context_object_name = 'teacher_list'
    
    

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    
    # success URL?
    success_url = reverse_lazy('classroom:thank_you')
    
    # what to do with form
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)