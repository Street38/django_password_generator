from django.shortcuts import render, HttpResponse
from random import choice
import string


# Create your views here.

def home(request):
    return render(request, "generator/home.html")


def general_password(request):
    chars_all = string.ascii_lowercase
    result_password = ''
    lengh = request.GET.get('len')
    if request.GET.get('up'):
        chars_all = string.ascii_letters
    if request.GET.get('num'):
        chars_all += string.digits
    if request.GET.get('spec'):
        chars_all += string.punctuation
    for i in range(int(lengh)):
        result_password += choice(chars_all)
    return render(request, "generator/password.html", {"password": result_password})


def about(request):
    return render(request, "generator/about.html")
