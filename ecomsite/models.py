from django.db import models

# Create your models here.
class Employee(models.Model):
    designation = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=12,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.Name