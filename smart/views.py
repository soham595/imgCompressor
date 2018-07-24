from django.shortcuts import render
from .models import Image
import numpy as np
from MLDjango import new_net_classif


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

def saveWeight(request):
    new_net_classif.train_model()
    return render(request, 'smart/train.html')


def checkForLiver(request):
    x = np.array([[2], [3], [4], [5], [6], [20]])
    xyz=new_net_classif.check(x)
    if xyz==True:
        print("whoops")
    else:
        print("Hooray")