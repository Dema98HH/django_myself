from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    department = models.ForeignKey(
        "department.Department",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.email


# class Record(models.Model):
#
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)
#     address = models.CharField(max_length=300)
#     city = models.CharField(max_length=100)
#     province = models.CharField(max_length=200)
#     country = models.CharField(max_length=255)
#     creations_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__ (self):
#         return f"{self.first_name} {self.last_name}"
