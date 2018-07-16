# Create your views here.
from django.shortcuts import render
from django.db import IntegrityError


def home(request):
    return render(request, '../templates/smart/index.html')