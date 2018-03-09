from __future__ import unicode_literals
from django.db import models

import bcrypt
import re

valid_email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
valid_name_regex = re.compile(r'[a-zA-Z]{2,}')
valid_passwd_regex = re.compile('(?=.*\d)(?=.*[a-z])[a-zA-Z0-9]{8,}')


def validate_input(firstname, lastname, password, confirmation, email, action):
    messages = []
    valid_entry = False

    if not valid_name_regex.match(firstname) or not valid_name_regex.match(lastname):
        messages.append(
            {
                "message": "Invalid first or last name format or entries are empty!",
                "message_tag": "{}_username_validation".format(action)
            }
        )

    elif not valid_passwd_regex.match(password):
        messages.append(
            {
                "message": "Password must be alphanumeric and at least eight characters long!",
                "message_tag": "{}_password_validation".format(action)
            }
        )

    elif not password == confirmation:
        messages.append(
            {
                "message": "Password and confirmation do not match! Please try again!",
                "message_tag": "{}_password_conf_validation".format(action)
            }
        )
    elif not valid_email_regex.match(email) or not email:
        messages.append(
            {
                "message": "Invalid email entry or is empty!",
                "message_tag": "{}_email_validation".format(action)
            }
        )
    else:
        valid_entry = True

    return messages, valid_entry

def encrypt_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

class UserManager(models.Manager):
    def validate_login(self, post):
        # Initializes the regular expressions to be used in validation of POST entries.

        messages = []
        user_validated = False
        action = "login"

        if not post['email_address'] or not valid_email_regex.match(post['email_address']):
            messages.append(
                {
                    "message": "Invalid email format or is empty!",
                    "message_tag": "{}_email_validation".format(action)
                }
            )

        if not post['user_password']:
            messages.append(
                {
                    "message": "Password cannot be empty!",
                    "message_tag": "{}_password_validation".format(action)
                }
            )

        if not messages:
            # Returns a user object where the email matched.
            try:
                user = User.objects.get(email=post['email_address'])
                if bcrypt.checkpw(post['user_password'].encode(), user.password.encode()):
                    messages.append(
                        {
                            "message": "Success! Welcome, {}!".format(user.first_name, user.last_name),
                            "message_tag": "valid_user"
                        }
                    )
                    user_validated = True

            except Exception:
                messages.append(
                    {
                        "message": "Invalid user! Try to register.",
                        "message_tag": "user_validation"
                     }
                )

        return messages, user_validated

    def validate_registration(self, post):
        name = post['first_name']
        lname = post['last_name']
        password = post['user_password']
        pw_confirmation = post['user_password_conf']
        email = post['email_address']
        action = "registration"

        return validate_input(name, lname, password, pw_confirmation, email, action)

    def new_user(self, post):
        messages = []
        user = None

        try:
            User.objects.get(email=post['email_address'])
            messages.append(
                {
                    "message": "Invalid email {}".format(post['email_address']),
                    "message_tag": "invalid_user"
                }
            )
        except Exception:

            # Encrypts the new users password
            hashed_password = encrypt_password(post['user_password'])

            # Creates this user.
            user = User.objects.create(first_name=post['first_name'], last_name=post['last_name'], email=post['email_address'],
                                   password=hashed_password, password_confirmation=hashed_password)
            messages.append(
                {
                    "message": "Success! Welcome, {}!".format(user.first_name, user.last_name),
                    "message_tag": "valid_user"
                }
            )

        return messages, user



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    password_confirmation = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return "User name: {} {} ".format(self.first_name,self.last_name)
