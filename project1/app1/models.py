from django.db import models

class Order(models.Model):
    oid=models.IntegerField(primary_key=True)
    oname=models.CharField(max_length=50)
    title=models.TextField()