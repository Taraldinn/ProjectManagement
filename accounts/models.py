from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver

# created user Custom Manager
class UserManager(BaseUserManager):
    # this function will create users objects
    def create_user(self, email, password, **extra_fields):
        if not email:
            # raise value error if email address is empty
            raise ValueError("A valid email address is required")

        user = self.model(
            email = self.normalize_email(email), # normalize submited email address
            **extra_fields
        )
        user.set_password(password) # set_password will converting char-password to hash
        user.save(using=self._db) # save user info to current database
        return user # finally return the user object

        # this function will create super user for admin
    def create_superuser(self, email, password, **extra_fields):
        # set all access to admin users
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'admin')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must be is_staff=True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('superuser must be is_active=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be is_superuser=True')
        
        return self.create_user(email, password, **extra_fields) # create super user object using create_user function
        


# created custom user models
class User(AbstractBaseUser, PermissionsMixin):
    # users type tuples
    USER_TYPE = (
        ('admin', 'admin'),
        ('leader', 'leader'),
        ('worker', 'worker')
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    user_type = models.CharField(max_length=100, choices=USER_TYPE, default='worker')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # we can pass extra fields on this list
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager() # called our custom manager here

    def __str__(self):
        return f"{self.email}" # return a string that we can see on dashboard

    class Meta:
        verbose_name_plural = "Users List" # verbose_name_plural will replace your models name



# created user profile models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # relation between user and profile models
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=False, null=False)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email # return a string that we can see on dashboard
    
    class Meta:
        verbose_name_plural = 'Users Profiles' # verbose_name_plural will replace your models name
    
    # signals functions
    """
    once a user object create,
    profile object will create for each user object
    """
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance) # creating profile object

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save() # save profile object