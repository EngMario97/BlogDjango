from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.name_category
