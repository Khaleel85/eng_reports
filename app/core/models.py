"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.createuser(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    CHOICES=(
        ('l', 'local'),
        ('e', 'expatriate')
    )
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    nationality=models.CharField(max_length=1, choices=CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'