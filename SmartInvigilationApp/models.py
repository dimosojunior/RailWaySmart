from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, phone, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        if not phone:
            raise ValueError("Your phone number is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, phone, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

  

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name", max_length=100, unique=False)
    phone=models.CharField(default="+255746244743", verbose_name="phone", max_length=13, unique=True)
    profile_image = models.ImageField(upload_to='get_profile_image_filepath', blank=True, null=True)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username','phone']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username



    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class InvigilationStaffs(models.Model):

	username = models.CharField(max_length=200,blank=False,null=False)
	email = models.EmailField(default="juniordimoso8@gmail.com", max_length=100,blank=False,null=False)
	camera_no = models.CharField(max_length=200,default="/videos/S1.mp4", blank=False,null=False)
	to_phone_number = models.CharField(default="+255746244743", max_length=13,blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.username