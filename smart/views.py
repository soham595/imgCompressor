from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import View
from .models import Image, LiverPatientInfo, BreastCancerPatientInfo
import numpy as np
import MLDjango.disease_liver as liver
import MLDjango.disease_bc as cancer
from .forms import UserForm



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
    # Insert functionality here
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

    x = np.array([[sex], [int(inp.total_bilirubin)], [int(inp.direct_bilirubin)], [int(inp.alkaline_phosphotase)],
                  [int(inp.alamine_aminotransferase)], [int(inp.albumin)]])
    xyz = liver.check(x)

    if xyz == True:
        dic = {"res": 1}
    else:
        dic = {"res": 0}

    inp.hasDisease = dic["res"]

    inp.save()
    print(inp.name)
    print(inp.hasDisease)
    print(inp.hasDisease == 1)

    return render(request, 'smart/output.html', {"result": inp})


def checkForBreastCancer(request):
    # id,"diagnosis","radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean",
    # "concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se",
    # "compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst",
    # "area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"

    bc = BreastCancerPatientInfo()
    bc.radius_mean = request.POST["rm"]
    bc.texture_mean = request.POST["tm"]
    bc.perimeter_mean = request.POST["pm"]
    bc.area_mean = request.POST["am"]
    bc.smoothness_mean = request.POST["sm"]
    bc.compactness_mean = request.POST["cm"]
    bc.concavity_mean = request.POST["ccm"]
    bc.concave_points_mean = request.POST["cpm"]
    bc.symmetry_mean = request.POST["sym"]
    bc.fractal_dimension_mean = request.POST["fdm"]
    bc.radius_se = request.POST["rs"]
    bc.texture_se = request.POST["ts"]
    bc.perimeter_se = request.POST["ps"]
    bc.area_se = request.POST["as"]
    bc.smoothness_se = request.POST["ss"]
    bc.compactness_se = request.POST["cs"]
    bc.concavity_se = request.POST["ccs"]
    bc.concave_points_se = request.POST["cps"]
    bc.symmetry_se = request.POST["sys"]
    bc.fractal_dimension_se = request.POST["fds"]
    bc.radius_worst = request.POST["rw"]
    bc.texture_worst = request.POST["tw"]
    bc.perimeter_worst = request.POST["pw"]
    bc.area_worst = request.POST["aw"]
    bc.smoothness_worst = request.POST["sw"]
    bc.compactness_worst = request.POST["cw"]
    bc.concavity_worst = request.POST["ccw"]
    bc.concave_points_worst = request.POST["cpw"]
    bc.symmetry_worst = request.POST["syw"]
    bc.fractal_dimension_worst = request.POST["fdw"]

    x1 = np.array([[bc.radius_mean], [bc.texture_mean], [bc.perimeter_mean], [bc.area_mean], [bc.smoothness_mean],
                   [bc.compactness_mean], [bc.concavity_mean], [bc.concave_points_mean], [bc.symmetry_mean],
                   [bc.fractal_dimension_mean],
                   [bc.radius_se], [bc.texture_se], [bc.perimeter_se], [bc.area_se], [bc.smoothness_se],
                   [bc.compactness_se], [bc.concavity_se], [bc.concave_points_se], [bc.symmetry_se],
                   [bc.fractal_dimension_se],
                   [bc.radius_worst], [bc.texture_worst], [bc.perimeter_worst], [bc.area_worst], [bc.smoothness_worst],
                   [bc.compactness_worst], [bc.concavity_worst], [bc.concave_points_worst], [bc.symmetry_worst],
                   [bc.fractal_dimension_worst]])

    xyz1 = cancer.check(x1)

    if xyz1 == True:
        dic = {"res": 1}
    else:
        dic = {"res": 0}

    bc.hasDisease = dic["res"]
    bc.save()

    return render(request, 'smart/output2.html', {"result": bc})


class UserFormView(View):
    #Specify the blueprint that we want to use
    form_class = UserForm

    #Specify html file where the form is to be included
    template_name = 'smart/register.html'

    #display blank form for new user
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #When user enters details and submits the form, process form data, register user and add them to database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #clean or normalize data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return user object if credentials are right
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('smart:index')

        return render(request, self.template_name, {'form': form})






def logout_user(request):

    logout(request)

    form = UserForm(request.POST or None)

    context = {

        "form": form,

    }

    return render(request, 'smart/login.html', context)





def login_user(request):

    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:

                login(request, user)

                return render(request, 'smart/index.html')

            else:

                return render(request, 'smart/login.html', {'error_message': 'Your account has been disabled'})

        else:

            return render(request, 'smart/login.html', {'error_message': 'Invalid login'})

    return render(request, 'smart/login.html')
