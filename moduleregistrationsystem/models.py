from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Module(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(1)], default='null')
    code = models.CharField(max_length=20, validators=[MinLengthValidator(1)], default='null')
    credit = models.IntegerField(default='60')
    category = models.CharField(max_length=100, validators=[MinLengthValidator(1)], default='null')
    description = models.TextField(validators=[MinLengthValidator(1)], default='null')
    availability = models.CharField(max_length=10, choices=[('Open', 'Open'), ('Closed', 'Closed')], default='open')
    courses_allowed = models.CharField(max_length=20, choices=[('Computing', 'Computing'), ('Biomedical Science', 'Biomedical Science'), ('Education', 'Education')], validators=[MinLengthValidator(1)], default='null')
    users = models.ManyToManyField(User, blank=True)

