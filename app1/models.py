from django.db import models
# student management system give me alternetive names for this project
# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.TextField(max_length=100)
    marks = models.IntegerField()
    age = models.IntegerField()
    def __str__(self):
        return self.name



from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.IntegerField(primary_key=id)
    name = models.TextField(max_length=45)
    age = models.IntegerField()
    dept = models.TextField(max_length=50)
    salary = models.IntegerField()
    def __str__(self):
        return self.name



 