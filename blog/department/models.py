import uuid

from django.db import models


class Department(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    department_name = models.CharField(max_length=100)


    def __str__ (self):
        return f"Department: {self.department_name}"