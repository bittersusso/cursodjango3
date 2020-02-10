from django.db import models

# Create your models here.

class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    deleted = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.subtitle

    full_name.admin_order_field = 'title'
    