from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

def basen(request):
    return render(request, 'basen.html')

def contact(request):
    return render(request, 'contact.html')


def aboutUs(request):
    return render(request, 'about_us.html')

def gallery(request):
    return render(request, 'gallery.html')

def example(request):
    return render(request, "example.html")

def typesOfPools(request):
    return render(request, "types_of_pools.html")