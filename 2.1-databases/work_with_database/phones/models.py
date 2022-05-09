from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100),
    price = models.IntegerField(),
    image = models.ImageField(),
    release_date = models.CharField(max_length=100),
    lte_exists = models.CharField(max_length=100),
    slug = models.SlugField(db_column=name)

