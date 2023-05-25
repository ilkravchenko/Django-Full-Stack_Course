from django.db import models
from django.db.models import Q

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} - {self.age} years old."
    
    
############################## Create database objects ##########################

# carl = Patient(first_name="Carl", last_name="Lebovsky", age=18)
# carl.save() save object in database
# Patient.objects.create(first_name='Illia', last_name="Kravchenko", age=20)
# my_list = [Patient(first_name="Lil", last_name="Peep", age=21),
#           Patient(first_name="Ilya", last_name="Lebovskyi", age=21)
#           Patient(first_name="Lili", last_name="Baby", age=18)]
# Patient.objects.bulk_create(my_list)

# ############################ Read data from database ###################################

# # pick all items from database
# # Patient.objects.all() #return list of objects

# # pick a single item form database
# Patient.objects.get(pk=1)

# # pick some data by filtering
# Patient.objects.filter(last_name='Kravchenko').get() 
# Patient.objects.filter(last_name='Kravchenko').all() 
# Patient.objects.filter(last_name='Kravchenko').filter(age=20).get() 

# # filtering with Q
# Patient.objects.filter(Q(last_name='smith') & Q(age=20)).all()

# ####################### Fields Lookups #############################################

# Patient.objects.filter(last_name__startwith='s').all()
# Patient.objects.filter(age__in=[20,30]).all()
# Patient.objects.filter(age__gte=39).all()
# Patient.objects.filter(age__lt=20).all()

# # ordering
# Patient.objects.filter(age__lt=20).all().order_by('age') 
