# Code taken from the CodeInstitute Walkthrough 'I think, therefor I blog'
# and slightly moified
from django.db import models
from cloudinary.models import CloudinaryField

class About(models.Model):
    """

    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    about_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f'{self.title}'

class ContactRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message through contact form request from {self.name}"