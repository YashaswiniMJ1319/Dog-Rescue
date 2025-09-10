from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    age = models.IntegerField()
    status = models.CharField(max_length=20, choices=[
        ('Missing', 'Missing'),
        ('Found', 'Found'),
        ('Adopted', 'Adopted')
    ])
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dog_images/')
    
    def __str__(self):
        return self.name

class IssueReport(models.Model):
    user = models.CharField(max_length=100)  # Change to ForeignKey if using authentication
    email = models.EmailField()
    message = models.TextField()
    resolved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Issue from {self.user}"
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)  # Store as plain text (not secure, just for learning)
    

    def __str__(self):
        return self.name
class ContactInfo(models.Model):
    phone = models.CharField(max_length=20, default="")
    email = models.EmailField(default="")
    address = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"Contact Info: {self.email}"
class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    phone_number = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self) :
        return self.name
# Example in models.py
from django.db import models

class ContactInfo(models.Model):
    name = models.CharField(max_length=150, default="")
    email = models.CharField(max_length=150, default="")
    phone_number = models.CharField(max_length=15, default="")
    message = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name

# Create your models here.
