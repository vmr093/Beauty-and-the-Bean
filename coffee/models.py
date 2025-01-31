from django.db import models

# Create your models here.

class Coffee(models.Model):
    name = models.CharField()
    description = models.TextField()
    image = models.ImageField(upload_to="photos/")

    def _str_(self):
        return self.name