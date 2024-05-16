from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

import uuid

# user manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address.')
    
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.auth_provider="local"
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# User
class User(AbstractBaseUser):
    id = models.UUIDField(default=uuid.uuid4, blank=False,
                          null=False, unique=True, primary_key=True, editable=False)

    email = models.EmailField(unique=True, max_length=150)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    is_blogger = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
