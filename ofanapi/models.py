from django.db import models
from django.utils import timezone


class Homes(models.Model):
    """ model for registering an orphanage"""
    home_name = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="Mombasa, Likoni")
    capacity = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """return formatted string"""
        return self.home_name

    class Meta:
        verbose_name_plural = "Homes"


class Groups(models.Model):
    """ model for creating groups"""
    group_name = models.CharField(max_length=100, unique=True)
    home_name = models.ForeignKey(Homes, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=100)
    visit_date = models.DateTimeField()

    def __str__(self):
        """ return formatted string"""
        return self.group_name

    class Meta:
        verbose_name_plural = "Groups"


class Join_Group(models.Model):
    """ Models for a user to join group"""
    group_name = models.ForeignKey(Groups, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=13)

    def __str__(self):
        """ return formatted string"""
        return self.member_name

    class Meta:
        verbose_name_plural = "Join_Group"