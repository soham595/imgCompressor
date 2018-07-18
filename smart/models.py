from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    iname = models.CharField(max_length=30)

    def __str__(self):
        return self.iname
