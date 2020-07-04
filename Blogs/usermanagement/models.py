from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser, PermissionsMixin, UserManager
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import models as auth_models

class CustomModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)

    @classmethod
    def get_field_names(cls):
        field_names = list()
        for field in CustomModel._meta.fields:
            field_names.append(field.attname)
        return field_names

    class Meta:
        abstract = True

class CustomUserManager(UserManager, BaseUserManager):

    @staticmethod
    def is_user_exists(email):
        user = CustomUser.objects.filter(email=email).first()
        return user



    def create_user_custom(self, email, password, first_name, last_name, is_staff, is_active=True):
        user = self.model(
            email=CustomUserManager.normalize_email(email),
            username="",
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_active=is_active,
        )
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, CustomModel, PermissionsMixin):
    username = models.CharField(max_length=25, blank=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=datetime.now())
    last_login = models.DateTimeField(_('last login'), blank=True, default=datetime.now())
    is_staff = models.BooleanField(
        _('staff status'),
        default=False
    )
    is_active = models.BooleanField(
        _('active'),
        default=True
    )
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def get_short_name(self):
        return self.first_name

    @classmethod
    def get_user_object(cls, user_email):
        user_obj = User.objects.get(email=user_email)
        return user_obj

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'


auth_models.User = CustomUser
