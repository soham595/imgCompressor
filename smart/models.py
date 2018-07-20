from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    iname = models.CharField(max_length=30)

    def __str__(self):
        return self.iname


class PatientInfo(models.Model):
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

    def __str__(self):
        return self.name

