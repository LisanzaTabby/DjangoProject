from django.db import models

class Student(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices= GENDER)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'