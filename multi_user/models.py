from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.Model):
    STUDENT = 1
    TEACHER = 2
    SECRETARY = 3
    SUPERVISOR = 4
    ADMIN = 5

    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (SECRETARY, 'secretary'),
        (SUPERVISOR, 'supervisor'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)


class User(AbstractUser):
    roles = models.ManyToManyField(Role)



