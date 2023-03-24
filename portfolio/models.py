from django.db import models

class Prospect(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
