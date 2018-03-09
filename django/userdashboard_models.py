from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+[@a-sA_Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Managers
class UserManager(models.Manager):

    # method for inserting a user
    def registration_validator(self, postData):
        errors = {}
        #TODO add validations
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']
        password = postData['password']
        confirm = postData['cPassword']

        if len(password) < 8:
            errors["password"] = "Password must be greater than 8 characters!"

        if confirm != password:
            errors["cPassword"] = "Passwords did not match!"

        if not re.match(NAME_REGEX, first_name) or not re.match(NAME_REGEX, last_name):
            errors["name"] = "Name field must only contain letters!"

        if not re.match(EMAIL_REGEX, email):
            errors["email"] = "Email is not valid!"
        else:
            if len(self.filter(email=email)) >= 1:
                errors["email"] = "Email is already registered!"

        if not errors:
            hashedPw = bcrypt.hashpw((password.encode()), bcrypt.gensalt(5))

            new_user = self.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = hashedPw
            )

            return new_user

        return errors

        def login_validator(self, postData):
            errors = {}
            email = postData['email']
            password = postData['password']

            if len(value < 1):
                errors[field] = "Email/password field cannot be empty!"
                return errors

            if len(self.filter(email)) > 0:
                user = User.objects.get(email = email)
                if not bcrypt.checkpw(password.encode(), user.password.encode()):
                    errors["password"] = "email/password does not match records!"

            if errors:
                return errors

            return user

class User(models.Model):
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255)
    user_level = models.IntegerField()

    objects = UserManager()

class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, related_name="sent_messages")
    receiver = models.ForeignKey(User, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, related_name="sent_comments")
    comment_message = models.ForeignKey(Message, related_name="message_comments")

    objects = UserManager()
