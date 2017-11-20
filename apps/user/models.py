from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy


class User(AbstractUser):
    email = models.EmailField(ugettext_lazy('email address'), unique=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'auth_user'
