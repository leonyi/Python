from __future__ import unicode_literals
from django.db import models


import bcrypt
import re

class AdminManager(models.Manager):
    def validate_admin(self, post):
        errors = {
            "error": "",
            "error_tag": ""
        }

        email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')

        if not email_regex.match(post['email_address']):
            errors['error'] = "Invalid email format!"
            errors['error_tag'] = "email_validation"
        else:
            admin = Admin.objects.first()

            print "{} - {}".format(admin.email, post['email_address'])

            if admin.email == post['email_address']:
                if bcrypt.checkpw(post['user_password'].encode(), admin.password.encode()):
                    errors = "valid email"
                else:
                        errors['error'] = "Password is incorrect!"
                        errors['error_tag'] = "password_validation"
            else:
                 errors['error'] = "Incorrect email!"
                 errors['error_tag'] = "email_validation"

        return errors



class UserManager(models.Manager):
    def validate(self, post):
        errors = {
            "error": "",
            "error_tag": ""
        }
        valid_email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
        valid_name_regex = re.compile(r'[a-zA-Z]{2,}')

        if not valid_name_regex.match(post['first_name']) or not valid_name_regex.match(post['last_name']):
            errors['error'] = 'First and last name must only contain characters or is too short!'
            errors['error_tag'] = 'name_validation'
        elif not valid_email_regex.match(post['email']):
            errors['error'] = 'Invalid email entry!'
            errors['error_tag'] = 'email_validation'
        else:
            errors = False

        print "In validate errors are: {}".format(errors)

        return errors

    def update_entry(self, post):
        user = User.objects.get(id=post['hidden'])
        if post['first_name']:
            print "Updating user with {}".format(post['first_name'])
            user.first_name = post['first_name']
        if post['last_name']:
            user.last_name = post['last_name']
        if post['email']:
            user.email = post['email']

        user.save()

        return True

    def entry_exists(self, post):
        found = User.objects.filter(email=post['email'])

        if found:
            return True
        else:
            return False

    def create_entry(self,post):
        uid = User.objects.create(first_name=post['first_name'], last_name=post['last_name'], email=post['email'],
                                  admin_id=1)

        return uid.id


class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AdminManager()

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin = models.ForeignKey(Admin, related_name="admin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

