from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.subtitle

    full_name.admi
    