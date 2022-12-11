from django.db import models
# Create your models here.

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='', null=True, verbose_name="")
    reqs= models.CharField(max_length=500)
    def __str__(self):
        return self.name + ": " + str(self.videofile)