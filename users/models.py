from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=255)
    city_town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    course = models.CharField(null=True, max_length=50)
    module_Selection_1_ID_Number = models.IntegerField(null=True)
    module_Selection_2_ID_Number = models.IntegerField(null=True)
    

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


