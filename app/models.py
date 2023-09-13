from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class info(models.Model):
        name = models.CharField(max_length=30)
        age = models.IntegerField(default=0)

 

class MyUserManager(BaseUserManager):
    def create_user(self,username ,key,password=None):
         
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        user.info  = key
        return user

    def create_superuser(self, username, password=None):
      
        user = self.model(username=username)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    info = models.ForeignKey(info, on_delete=models.CASCADE ,null=True,default=None)

    objects = MyUserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username


    @property
    def is_staff(self):
        return self.is_admin
    

