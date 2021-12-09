from django.db import models
from django.db.models.fields import BigIntegerField

# Create your models here.
class student (models.Model):
    id = models.IntegerField()
    first_name = models.VARCHAR(50)
    last_name = models.VARCHAR(50)
    code = models.CharField(10)
    created_at = models.DateTimeField

    class subjets(models.Model):
        id = models.IntegerField
        name = models.CharField(50)
        code = models.CharField(50)
        course = models.CharField(3)
        created_at = models.DateTimeField

    class subject(models.Model):
        id = models.IntegerField
        id_student = models.IntegerField
        id_subject = models.IntegerField
        created_at = models.DateTimeField