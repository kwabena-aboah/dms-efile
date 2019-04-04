from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	owner = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE,)
	picture = models.ImageField(upload_to='Uploads/profiles', blank=True)

	def __str__(self):
		return self.user