from django.shortcuts import render
from .models import Image, LiverPatientInfo
import numpy as np
import MLDjango.disease_liver as liver
import MLDjango.disease_bc as cancer



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


def saveWeightLiver(request):
    liver.train_model()
    return render(request, 'smart/train.html')

def saveWeightBc(request):
    cancer.train_model()
    return render(request, 'smart/train.html')


def checkForLiver(request):

    inp = LiverPatientInfo()
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
    xyz = liver.check(x)

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
    #return render(request, 'smart/output.html')

def checkforbcancer(request):




    x1=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],
                 [11],[12],[13],[14],[15],[16],[17],[18],[19],[20],
                 [21],[22],[23],[24],[25],[26],[27],[28],[29],[30]])
    xyz1=cancer.check(x1)

    if xyz1==True:
        dic = {"res": 1}
    else:
        dic = {"res": 0}

