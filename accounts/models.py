from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True)
    image = models.ImageField(upload_to="accounts/profile/", null=True)

    def get_project_url(self):
        return reverse('profile', kwargs={"pk": self.id})
