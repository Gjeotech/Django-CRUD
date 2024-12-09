from django.db import models

# Create your models here.

class Record(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    profile_image = models.ImageField(upload_to="images/", blank=True, null=True)

#now that we hv added image variable, we will re-run migration anagin
