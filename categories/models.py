from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, default='default/default.jpg')

    def __str__(self):
        return self.name
