from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
import datetime

class CustomUser(AbstractUser):
	date_of_birth = models.DateField()
	GENDER = (
		('m', 'Male'),
		('f', 'Female'),
		('o', 'Other'),
	)
	gender = models.CharField(max_length=1, choices=GENDER, default='m')