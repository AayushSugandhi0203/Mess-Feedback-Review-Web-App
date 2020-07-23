from django.db import models

# Create your models here.

class Menupdf(models.Model):
    title = models.CharField(max_length = 20)
    filepdf = models.FileField(upload_to='pdfs')
    
    
class Feedback(models.Model):
    name = models.CharField(max_length = 50)
    entry = models.CharField(max_length = 50)
    date = models.DateField(max_length = 50)
    meal = models.CharField(max_length = 50)
    text = models.CharField(max_length = 100)
    review = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    
    
