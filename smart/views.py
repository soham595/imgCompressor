from django.shortcuts import render
from .models import Image, LiverPatientInfo
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
    inp = LiverPatientInfo()
    inp.name = request.POST["name"]
    inp.gender = request.POST["gender"]
    inp.total_bilirubin = request.POST["tb"]
    inp.direct_bilirubin = request.POST["db"]
    inp.alkaline_phosphotase = request.POST["ap"]
    inp.alamine_aminotransferase = request.POST["aa"]
    inp.albumin = request.POST["alb"]
    inp.save()
    sex = 0
    if inp.gender == 'F':
        sex = 1


    x = np.array([[sex], [int(inp.total_bilirubin)], [int(inp.direct_bilirubin)], [int(inp.alkaline_phosphotase)], [int(inp.alamine_aminotransferase)], [int(inp.albumin)]])
    xyz = new_net_classif.check(x)


    #inp.hasDisease = res

    if xyz==True:
        dic = {"res":1}
    else:
        dic = {"res":0}

    return render(request, 'smart/predictionLiver.html', dic)
