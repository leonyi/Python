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
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    print "in encrypt_password hashed password is {}".format(hashed)

    return hashed

class UserManager(models.Manager):
    def validate_login(self, post):

        messages = []
        user_validated = False
        found = ""
        action = "login"

        if not valid_email_regex.match(post['email_address']) or not post['email_address'] :
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
        else:
            # Returns a user object where the email matched.
            try:
                found = User.objects.get(email=post['email_address'])
            except Exception:
                messages.append(
                    {
                        "message": "Invalid user! Try to register.",
                        "message_tag": "user_validation"
                     }
                )


            if found and found.email == post['email_address']:
                # To do: Find out how to call class methods from other methods within the same class.
                # passwords_match = check_password(post)
                passwords_match = bcrypt.checkpw(post['user_password'].encode(), found.password.encode())

                if passwords_match:
                    messages.append(
                        {
                            "message": "Success! Welcome, {}!".format(found.first_name, found.last_name),
                            "message_tag": "valid_user"
                        }
                    )
                    user_validated = True

                    print


        return messages, user_validated

    def validate_registration(self, post):
        name = post['first_name']
        lname = post['last_name']
        password = post['user_password']
        pw_confirmation = post['user_password_conf']
        email = post['email_address']
        action = "registration"

        errors, valid_entry = validate_input(name, lname, password, pw_confirmation, email, action)

        return errors, valid_entry

    def new_user(self, post):
        messages = []
        found_user = False

        try:
            get_user = User.objects.get(email=post['email_address'])
            found_user = True
        except Exception:
            # If not found! Great we can add this user.
            pass

        if found_user is False:
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

        return messages



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
