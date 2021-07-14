from django.db import models
import re

from django.db.models.deletion import CASCADE

# Create your models here.
class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        if len(reqPOST['user_name']) < 3:
            errors['user_name'] = "Name is too short"
        if len(reqPOST['email']) < 6:
            errors['email'] = "Email is too short"
        if len(reqPOST['password']) <8:
            errors['password'] = "Password is too short"
        if reqPOST['password'] != reqPOST['password_conf']:
            errors['match'] = "Passwords don't match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST['email']):
            errors['regex'] = "Email in wrong format"
        users_with_email = User.objects.filter(email=reqPOST['email'])
        if len(users_with_email) >= 1:
            errors['dup'] = "Email taken, use another"
        return errors

class GiraffeManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        if len(reqPOST['giraffe_name']) < 3:
            errors['giraffe_name'] = "Name is too short"
        if len(reqPOST['catchphrase']) < 3:
            errors['catchphrase'] = "Catchphrase is too short"
        giraffes_with_name = Giraffe.objects.filter(name=reqPOST['giraffe_name'])
        if len(giraffes_with_name) >= 1:
            errors['dup'] = "Name taken, use another"
        return errors

class User(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



class Giraffe(models.Model):
    name = models.TextField()
    catchphrase = models.TextField()
    owner = models.ForeignKey(User, related_name="giraffes_owned", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GiraffeManager()
