from django.shortcuts import render
from .models import Image

def home(request):
    return render(request, 'smart/index.html')

def imageUpload(request):
    image = Image()
    image.image = request.FILES['image']
    image.iname = request.POST['iname']
    image.save()
    dict = {'image': image}
    return render(request, 'smart/index.html', dict)

def imageView(request, foo):
    image = Image.objects.get(pk=foo)
    dict = {'image': image}
    return render(request, 'smart/index.html', dict)

def trainView(request):
    #Insert functionality here
    return render(request, 'smart/train.html')
