from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse

from .managers import CustomUserManager

ROLE_CHOICES = (
    ('', 'Please Select Role'),
    ('master', 'Master'),
    ('teacher', 'Teacher'),
    ('secretary', 'Secretary'),
    ('accountant', 'Accountant'),
    ('hr', 'Human Resource'),
    ('librarian', 'Librarian'),
    ('academy', 'Academy'),
    ('matron', 'Matron'),
    ('vehicle', 'Vehicle'),
)

class CustomUser(AbstractBaseUser):
    name = models.CharField(verbose_name='Full Name', max_length=100)
    email = models.EmailField(
        verbose_name='Email Address', unique=True, max_length=100)
    role = models.CharField(verbose_name='What primary role?', max_length=40, choices=ROLE_CHOICES)

    created_by = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser

    def __str__(self):
        return self.email

    def _send_welcome_mail(self):
        # send mail here
	    pass


# Profile Picture
def profile_pic_filename(instance, filename):
    ext = filename.split('.')[1]
    new_filename = f'{uuid4()}.{ext}'
    return f'profile_pics/{new_filename}'


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, primary_key=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(verbose_name='Profile Picture',
                                    default='profile_pics/user.svg',
                                    upload_to=profile_pic_filename)

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'pk': self.user_id})

    def get_profile_update_url(self):
        return reverse('users:profile-update', kwargs={'pk': self.user_id})

    def __str__(self):
        return f'{self.user.name} Profile'

