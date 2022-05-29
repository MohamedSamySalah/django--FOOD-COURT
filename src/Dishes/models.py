from distutils.command.upload import upload
from pickle import TRUE
from django.db import models
from django.utils.text import slugify

# Create your models here.


def customise_image(instance,image):
    image_name , extension = image.split(".")
    return f"Resturant/{instance.id}.{extension}"


class Resturants(models.Model):
   
    Resturants_status = (
        ('Open','Open'),
        ('Close','Close'),
    )
    Restaurant_name = models.CharField(max_length=20)
    status =models.CharField(max_length=5,choices=Resturants_status)
    Description = models.TextField(max_length=50)

    # Phone
    # Rate
    # phone=models.models.CharField(max_length=15)

    image = models.ImageField(upload_to=customise_image) 
    slug=models.SlugField(blank=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.Restaurant_name)
        super(Resturants,self).save(*args,**kwargs)

    def __str__(self):
        return self.Restaurant_name



class category(models.Model):
    name_category = models.CharField(max_length=30)
    Resturants=models.ManyToManyField(Resturants,blank=True,related_name='Resturants_category')
    
    def __str__(self):
        return self.name_category




class Dishes(models.Model):
    Dish_Size=(
        ('Single','Single'),
        ('Double','Double'),
        ('Trible','Trible'),
    )
    # 666,66
    Dish_name = models.CharField(max_length=35)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=6,choices=Dish_Size,null=True,blank=True)
    category = models.ForeignKey(category,related_name="category_dishes", on_delete=models.PROTECT)
    Description = models.TextField(max_length=50)
    Restaurant = models.ForeignKey(Resturants,related_name="Restaurant_dishes",on_delete=models.PROTECT) 
    # Rate
    # time
    image =models.ImageField(upload_to=customise_image)


    def __str__(self):
        return self.Dish_name

    

