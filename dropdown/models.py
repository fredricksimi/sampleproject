from django.db import models

class DropdownModel(models.Model):
    CHOICES = (
        ('Today', 'Today'),
        ('Yesterday', 'Yesterday'),
        ('Custom', 'Custom')
    )
    event = models.CharField(max_length=50, default='')
    date_range = models.CharField(max_length=50, choices=CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
