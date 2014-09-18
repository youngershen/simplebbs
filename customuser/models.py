import time
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
class UserManager(BaseUserManager):
    
    def create_user(self, username = None, password = None, email = None):
        if username is None or password is None or email is None:
            raise ValueError('username and password and email are all required')

        user = self.model(username = username, email = email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        user = self.create_user(username= username, password = password, email = email)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def _get_file_dir(instance, filename):
    fmt_time = time.strftime('%y/%m/%d/%H/%m/', time.localtime(time.time()))
    username = instance.user.username
    path = username + '/' +fmt_time + filename
    return path


class User(AbstractBaseUser, PermissionsMixin):
    MALE    = 'male'
    FEMALE  = 'female'
    SHEMALE = 'shemale'
    DEFAULT = 'unknown'
    GENDER_CHOICES = (
            (MALE, 'male'),
            (FEMALE, 'female'),
            (SHEMALE, 'shemale'),
            (DEFAULT, 'unknown')
            )

    username  = models.CharField( max_length = 255, null = False, blank = False, unique = True)
    email     = models.EmailField(max_length = 255, unique = True, null  = False, blank = False)
    avatar    = models.ImageField(upload_to = _get_file_dir, null = True, blank = True)
    gender    = models.CharField(max_length = 10, choices = GENDER_CHOICES, default = DEFAULT)
    is_active = models.BooleanField(default = True)
    is_staff  = models.BooleanField(default = True)
    is_admin  = models.BooleanField(default = False)
    create_time     = models.DateTimeField(auto_now_add = True)
    modified_time   = models.DateTimeField(auto_now = True)
    first_name      = models.CharField(max_length = 255, null = True, blank = True)
    last_name       = models.CharField(max_length = 255, null = True, blank = True)
    objects         = UserManager()
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']


    def get_short_name(self):
        return  '{first_name} {last_name}'.format(first_name = self.first_name, last_name = self.last_name)    
    
    class Meta:
        ordering = ['-create_time']
        verbose_name = 'user'
        verbose_name = 'users'
