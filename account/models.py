from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.hashers import make_password


# Create your models here.

class Student(AbstractUser):
    phone_number = models.CharField(max_length=100)

    # USERNAME_FIELD = phone_number

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Token(models.Model):
    token = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)


class ExportEmployee(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.TextField()
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    user = models.OneToOneField(Student, on_delete=models.CASCADE, null=True, blank=True)
    activ = models.BooleanField(default=False)

    def __str__(self):
        return self.username
