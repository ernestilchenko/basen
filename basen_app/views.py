from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

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