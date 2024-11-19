from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def basen(request):
    return render(request, 'basen.html')
