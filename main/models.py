from django.db import models



class service(models.Model):
    icon=models.ImageField(),
    name=models.CharField(max_lenght=500),
    body=models.TextField()
    class Meta():
        verbose_name_plural="xizmatlar"

class meal(models.Model):
    name=models.CharField(max_leght=55),
    icon=models.ImageField(),
    body=models.TextField(),
    cost=models.CharField(max_lenght=50)
    class Meta():
        verbose_name_plural="taomlar"

class book(models.Model):
    name=models.CharField(max_lenght=255),
    email=models.EmailField(),
    data=models.DateTimeField(),
    people=models.CharField(max_lenght=3),
    body=models.TextField()
    class Meta():
        verbose_name_plural="buyurtma"
