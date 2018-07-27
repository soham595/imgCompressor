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

  ''' inp = LiverPatientInfo()
    inp.name = request.POST["name"]
    inp.age = request.POST["age"]
    inp.gender = request.POST["gender"]
    inp.total_bilirubin = request.POST["tb"]
    inp.direct_bilirubin = request.POST["db"]
    inp.alkaline_phosphotase = request.POST["ap"]
    inp.alamine_aminotransferase = request.POST["aa"]
    inp.aspartate_aminotransferase = request.POST["apa"]
    inp.total_proteins = request.POST["tp"]
    inp.albumin = request.POST["alb"]
    inp.albuminGlobulin_ratio = request.POST["abratio"]

    sex = 0
    if inp.gender == 'F':
        sex = 1


    x = np.array([[sex], [int(inp.total_bilirubin)], [int(inp.direct_bilirubin)], [int(inp.alkaline_phosphotase)], [int(inp.alamine_aminotransferase)], [int(inp.albumin)]])
    xyz = new_net_classif.check(x)

    if xyz==True:
        dic = {"res": 1}
    else:
        dic = {"res": 0}

    inp.hasDisease = dic["res"]

    inp.save()
    print(inp.name)
    print(inp.hasDisease)
    print(inp.hasDisease == 1)

    return render(request, 'smart/output.html', {"result": inp})

'''
  return render(request, 'smart/output.html')