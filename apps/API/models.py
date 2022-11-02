from django.db import models

class Pets(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    name = models.CharField(max_length=70, blank=False, default='')
    color = models.CharField(max_length=40, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    sex = models.CharField(max_length=10, blank=False, default='')
    age = models.IntegerField(blank=False, default=0)
