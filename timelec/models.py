from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True)

    def __str__(self):
        return self.name + ": " + str(self.videofile)
