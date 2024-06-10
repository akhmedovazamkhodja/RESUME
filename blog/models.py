from django.db import models

# Create your models here.


class MyWork(models.Model):
    name = models.TextField()
    app_cat = models.TextField()
    screenshot = models.ImageField()
    link = models.URLField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.date.year}.{self.date.month}.{self.date.day} - {self.date.hour}:{self.date.minute}'
