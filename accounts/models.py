from django.db.models import Sum
from django.conf import settings
from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    icon = models.CharField(max_length=254, default="icon")

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Budget(models.Model):

    total_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expenses = models.JSONField()
    date = models.DateTimeField(auto_now_add=True)

