from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class UserRoles(models.TextChoices):
    ADMIN = 'admin', 'Администратор'
    USER = 'users', 'Пользователь'


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Почта')
    role = models.CharField(max_length=20, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Роль')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
