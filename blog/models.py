from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title