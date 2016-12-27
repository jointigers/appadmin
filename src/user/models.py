from django.db import models
import ListField
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    first_name = models.CharField("person's first name", max_length=30)
    last_name = models.CharField("person's first name", max_length=30)
    '''
class Article(models.Model):
    labels = ListField.ListField()
    '''