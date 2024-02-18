from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=100)


    def __str__ (self):
        return f"Department: {self.department_name}"