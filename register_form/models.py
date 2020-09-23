from django.db import models


class SubmissionFormModel(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name
