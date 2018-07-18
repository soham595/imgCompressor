from django.shortcuts import render
from .models import Image

def home(request):
    return render(request, '../templates/smart/index.html')

def imageUpload(request):
    image = Image()
    image.image = request.FILES['image']
    image.iname = request.POST['iname']
    image.save()
    return render(request, 'smart/index.html')

def imageView(request, foo):
    image = Image.objects.get(pk=foo)
    dict = {'image': image}
    return render(request, 'smart/index.html', dict)