from django.db import models
class Services(models.Model):
    subject = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
    author = models.CharField(max_length=100)


class PDFFile(models.Model):
    file = models.FileField(upload_to='pdfs/')
    filename = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.filename
    
    
class Form(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.CharField( max_length=40)
    Subject=models.CharField(max_length=100)
    Message=models.TextField(max_length=500)




# Create your models here.
