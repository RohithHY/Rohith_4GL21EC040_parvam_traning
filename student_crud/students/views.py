from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "students/index.html")

def about_us(request):
    return render(request, "students/about-us.html")


def services(request):
    return render(request, "students/services.html")


def contact_us(request):
    return render(request, "students/contact-us.html")