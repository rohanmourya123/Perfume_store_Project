from django.db import models


# Create your models here.
class index(models.Model):
    brand = models.CharField(max_length=30,default="0")
    category = models.CharField(max_length=50,default="0")
    img = models.ImageField(upload_to="images",default="https://cdn.pixabay.com/photo/2017/07/02/19/24/dumbbells-2465478_960_720.jpg")
    price= models.IntegerField(default=0)
   # img = models.ImageField(upload_to= "/images",default="" )
    pub_date = models.DateField(null=True)
    name = models.CharField(max_length=100,default=0)
    description = models.CharField(max_length=200,default="0")

    def __str__(self):
        return self.name


class slider_images(models.Model):
    title= models.CharField(max_length=250)
    img = models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title