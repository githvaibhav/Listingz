from django.db import models
from django.utils.timezone import now
class Listings(models.Model):

    types_of_sales=(('For Sale', 'for_sale'),
                    ('For Rent', 'for_rent'),)
    

    types_of_homes=(('House', 'house'),
                    ('Condo', 'condo'),
                    ('TownHouse', 'townhouse'),)


    realtor= models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    slug= models.SlugField(unique=True)
    address= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    state= models.CharField(max_length=255)
    zipcode= models.CharField(max_length=10)
    description= models.TextField()
    price= models.IntegerField()
    bedrooms= models.IntegerField()
    bathrooms= models.DecimalField(max_digits=2, decimal_places=1)
    sale_type= models.CharField(max_length=10, choices=types_of_sales, default='For Sale' )
    home_type= models.CharField(max_length=10, choices=types_of_homes, default='House' )
    main_photo= models.ImageField(upload_to="listings/")
    photo1= models.ImageField(upload_to="listings/")
    photo2= models.ImageField(upload_to="listings/")
    photo3= models.ImageField(upload_to="listings/")
    is_published= models.BooleanField(default= False)
    date_created= models.DateField(default=now)

    def __str__(self):
        return self.title
