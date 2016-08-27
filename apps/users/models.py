from django.db import models
from django.utils.translation import ugettext
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class EmailUserManager(BaseUserManager):

    def create_user(self, *args, **kwargs):
        email = kwargs['email']
        email = self.normalize_email(email)
        password = kwargs['password']
        kwargs.pop('password')

        if not email:
            raise ValueError(ugettext('Users must have an email address'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name=ugettext('Email address'), 
        unique=True
    )
    first_name = models.CharField(
        verbose_name=ugettext('Name'),
        max_length=50,
        blank=False,
        help_text=ugettext('Inform your name')
    )
    last_name = models.CharField(
        verbose_name=ugettext('Last name'),
        max_length=50,
        blank=False,
        help_text=ugettext('Inform your last name')
    )
    USERNAME_FIELD = 'email'
    objects = EmailUserManager()
    