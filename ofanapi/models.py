from django.db import models
from django.utils import timezone


class Homes(models.Model):
    """ model for registering an orphanage"""
    home_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="Mombasa, Likoni")
    capacity = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """return formatted string"""
        return self.home_name

    class Meta:
        verbose_name_plural = "Homes"
