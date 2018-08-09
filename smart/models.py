from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    iname = models.CharField(max_length=30)

    def __str__(self):
        return self.iname


class LiverPatientInfo(models.Model):
    username = models.CharField(max_length=15, default="abc")
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    total_bilirubin = models.FloatField()
    direct_bilirubin = models.FloatField()
    alkaline_phosphotase = models.FloatField()
    alamine_aminotransferase = models.FloatField()
    aspartate_aminotransferase = models.FloatField()
    total_proteins = models.FloatField()
    albumin = models.FloatField()
    albuminGlobulin_ratio = models.FloatField()
    hasDisease = models.IntegerField()

    def __str__(self):
        return self.name

#id,"diagnosis","radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean",
# "concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se",
# "compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst",
# "area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"


class BreastCancerPatientInfo(models.Model):
    username = models.CharField(max_length=15, default="abc")
    radius_mean = models.FloatField()
    texture_mean = models.FloatField()
    perimeter_mean = models.FloatField()
    area_mean = models.FloatField()

    smoothness_mean = models.FloatField()
    compactness_mean = models.FloatField()
    concavity_mean = models.FloatField()
    concave_points_mean = models.FloatField()
    symmetry_mean = models.FloatField()
    fractal_dimension_mean = models.FloatField()
    radius_se = models.FloatField()
    texture_se = models.FloatField()
    perimeter_se = models.FloatField()
    area_se = models.FloatField()
    smoothness_se = models.FloatField()
    compactness_se = models.FloatField()
    concavity_se = models.FloatField()
    concave_points_se = models.FloatField()
    symmetry_se = models.FloatField()
    fractal_dimension_se = models.FloatField()
    radius_worst = models.FloatField()
    texture_worst = models.FloatField()
    perimeter_worst = models.FloatField()
    area_worst = models.FloatField()
    smoothness_worst = models.FloatField()
    compactness_worst = models.FloatField()
    concavity_worst = models.FloatField()
    concave_points_worst = models.FloatField()
    symmetry_worst = models.FloatField()
    fractal_dimension_worst = models.FloatField()
    hasDisease = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.username
