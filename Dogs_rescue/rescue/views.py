from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Dog

def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request,'login.html')

def dogs_by_name(request):
    dogs = Dog.objects.all().order_by('name')
    return render(request, 'dogs_by_name.html', {'dogs': dogs})

def dogs_by_breed(request):
    dogs = Dog.objects.all().order_by('breed')
    return render(request, 'dogs_by_breed.html', {'dogs': dogs})

def available_dogs(request):
    dogs = Dog.objects.filter(status='Found')
    return render(request, 'available_dogs.html', {'dogs': dogs})

def recent_dogs(request):
    dogs = Dog.objects.all().order_by('-id')[:10]
    return render(request, 'recent_dogs.html', {'dogs': dogs})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def dogs_by_name(request):
    dogs = Dog.objects.all().order_by('name')  # Query the Dog model
    return render(request, 'dogs_by_name.html', {'dogs': dogs})

from .forms import DogForm

def add_dog(request):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to your home page or a success page
    else:
        form = DogForm()
    return render(request, 'add_dog.html', {'form': form})
def dogs_by_status(request, status):
    # Validate the status to be one of the choices if necessary
    dogs = Dog.objects.filter(status=status)
    return render(request, 'dogs_by_status.html', {'dogs': dogs, 'status': status})
def filter_dogs(request):
    return render(request, 'filter_dogs.html')



def home(request):
    missing_dogs = Dog.objects.filter(status='Missing')
    found_dogs = Dog.objects.filter(status='Found')
    context = {
        'missing_dogs': missing_dogs,
        'found_dogs': found_dogs,
    }
    return render(request, 'home.html', context)

def dogs_by_status(request, status):
    # This filters dogs by the status parameter passed in the URL
    dogs = Dog.objects.filter(status=status)
    context = {
        'dogs': dogs,
        'status': status
    }
    return render(request, 'dogs_by_status.html', context)
from .models import ContactInfo




def missing_dogs(request):
    # For now, render a simple template or return a HttpResponse
    return render(request, 'missing_dogs.html')

        
    contact_entry.save()
    messages.success(request, "Thank you for reaching out. We will contact you soon!")
    return render(request, 'contact.html')
def missing_dogs(request):
    # Replace with actual logic
    missing = Dog.objects.filter(status='Missing')
    return render(request, 'missing_dogs.html', {'missing': missing})

def found_dogs(request):
    # Replace with actual logic
    found = Dog.objects.filter(status='Found')
    return render(request, 'found_dogs.html', {'found': found})

def adopted_dogs(request):
    # Replace with actual logic
    adopted = Dog.objects.filter(status='Adopted')
    return render(request, 'adopted_dogs.html', {'adopted': adopted})
def contact(request):
    if request.method == "POST":
        contact_name = request.POST.get('contactname', '')
        contact_email = request.POST.get('contactemail', '')
        contact_number = request.POST.get('contactnumber', '')
        contact_msg = request.POST.get('contactmsg', '')

        contact_entry = contact(
            name=contact_name,
            email=contact_email,
            phone_number=contact_number,
            message=contact_msg
        )
        contact_entry.save()
        messages.success(request, "Thank you for reaching out. We will contact you soon!")
    return render(request, 'contact.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactInfo  # Make sure ContactInfo is your model

def contact(request):
    if request.method == "POST":
        contact_name = request.POST.get('contactname', '')
        contact_email = request.POST.get('contactemail', '')
        contact_number = request.POST.get('contactnumber', '')
        contact_msg = request.POST.get('contactmsg', '')

        # Instantiate the ContactInfo model instead of calling the view function 'contact'
        contact_entry = ContactInfo(
            name=contact_name,
            email=contact_email,
            phone_number=contact_number,
            message=contact_msg
        )
        contact_entry.save()
        messages.success(request, "Thank you for reaching out. We will contact you soon!")
    return render(request, 'contact.html')



