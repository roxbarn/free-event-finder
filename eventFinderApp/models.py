from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    categories = models.ManyToManyField(Category)
    
    # def __str__(self):
    #     return self.title

    # def __str__(self):
    #     return self.location

    # def __str__(self):
    #     return self.start_time

    # def __str__(self):
    #     return self.end_time

    # def __str__(self):
    #     return self.categories

    # def get_categories(self):
    # ret = ''
    # print(self.categories.all())

class Category(models.Model):
    name = models.CharField(max_length=50)
    events = models.ManyToManyField(Event)
    
    # def __str__(self):
    #     return self.name



