from django.shortcuts import render, redirect
from datetime import timezone
import datetime
from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        # Length of the first name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least two characters long"

        # Length of the last name
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least two characters long"

        # Email matches format
        email_regex = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"
        elif not email_regex.match(postData['email']):
            errors['email'] = "Must be a valid email"

        # Email is unique
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors['duplicate'] = "That email is already in use"

        # Password was entered (less than 8)
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characers long"
        if postData['password'] != postData['confirm_password']:
            errors['mismatch'] = "Your passwords do not match"

        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])
        if len(existing_user) != 1:
            errors['email'] = "User does not exist."
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['mismatch'] = "Email and password do not match"
        # email has been entered
        if len(postData['email']) == 0:
            errors['email'] = "Email must be entered"
        # Password has been entered
        if len(postData['password']) < 8:
            errors['password'] = "An eight character password must be entered"
        # if the email and password match
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255, default='Robert')
    last_name = models.CharField(max_length=255, default='Johnson')
    email = models.CharField(max_length=255, default='kuyperhouse@gmail.com')
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class MessageManager(models.Manager):
    def message_validator(self, postData):
        errors = {}
        if len(postData['title']) <1:
            errors['title_check'] = "Review must be at least 1 character"
        if len(postData['review']) <5:
            errors['review_check'] = "Description must be at least 5 characters"
        return errors

class Author(models.Model):
    name = models.CharField(max_length=255, default='Robert')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Books(models.Model):
    title = models.CharField(max_length=255, default="Title")
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Reviews(models.Model):
    book_reviewed = models.ForeignKey(Books, related_name="reviews", on_delete=models.CASCADE, null=True)
    reviewer =models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    review = models.CharField(max_length=255, default="Review")
    rating = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()