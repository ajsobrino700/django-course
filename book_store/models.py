from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(default = "",max_length = 128)
    rating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(5)])
    author = models.CharField(null=True,max_length =100)
    is_bestselling = models.BooleanField(default=False)

