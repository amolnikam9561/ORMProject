from django.contrib import admin
from app1.models import Student
from app1.models import Employee
from app1.models import Product
 



# Register your models here.
admin.site.register(Student)
# obj = Student(rollno=201,name='Pravin',marks=85,age=25)
# obj.save()
# obj = Student(rollno=203,name='Sakshi',marks=81,age=23)
# obj.save()


 
admin.site.register(Employee)
# emp = Employee(id=201,name='Sunil',age=34,dept='Account',salary=2500)
# emp.save()
# emp = Employee(id=202,name='Kunal',age=32,dept='Marketing',salary=20000)
# emp.save()
# emp = Employee(id=203,name='Sambit',age=32,dept='Testing',salary=23000)
# emp.save()
# emp = Employee(id=204,name='Manoj',age=32,dept='Account',salary=70000)
# emp.save()
# emp = Employee(id=205,name='Pradip',age=33,dept='Testing',salary=3100)
# emp.save()
# emp = Employee(id=206,name='Anil',age=35,dept='Dev',salary=40000)
# emp.save()


admin.site.register(Product)
# obj = Product(name="Wireless Mouse",price=29.99,description="Ergonomic Wireless mouse with USB reciver")
# obj.save()