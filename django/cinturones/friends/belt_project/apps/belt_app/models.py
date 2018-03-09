from __future__ import unicode_literals
from django.db import models

import bcrypt
import re

valid_email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
valid_name_regex = re.compile(r'[a-zA-Z]{3,}')
valid_passwd_regex = re.compile('(?=.*\d)(?=.*[a-z])[a-zA-Z0-9]{8,}')

def validate_input(firstname, alias, password, confirmation, email, action):
    messages = []
    valid_entry = False

    if not valid_name_regex.match(firstname) or not valid_name_regex.match(alias):
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
        found = ""
        action = "login"

        if not valid_email_regex.match(post['email_address']) or not post['email_address']:
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
                passwords_match = bcrypt.checkpw(post['user_password'].encode(), found.password.encode())

                if passwords_match:
                    messages.append(
                        {
                            "message": "Success! Welcome, {}!".format(found.name),
                            "message_tag": "valid_user"
                        }
                    )

                    print "in login validation current user id: {} - name: {} alias: {} email: {}".format(found.id, found.name, found.alias, found.email)

        return messages, found

    def validate_registration(self, post):
        name = post['user_name']
        alias = post['alias']
        password = post['user_password']
        pw_confirmation = post['user_password_conf']
        email = post['email_address']
        action = "registration"

        print "In validate_registration name is {}".format(name)
        errors, valid_entry = validate_input(name, alias, password, pw_confirmation, email,  action)

        return errors, valid_entry

    def new_user(self, post):
        found_user = False
        user = ""

        try:
            User.objects.get(email=post['email_address'])
            found_user = True
        except Exception:
            # If not found! Great we can add this user.
            pass

        if found_user is False:
            # Encrypts the new users password
            hashed_password = encrypt_password(post['user_password'])

            # Creates this user.
            user = User.objects.create(name=post['user_name'], alias=post['alias'], email=post['email_address'],
                                   password=hashed_password, birth_date=post['birth_date'])

            print "In new_user user is: {}".format(user.name)

        return user


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birth_date = models.DateField(default="1970-01-01")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


    def __str__(self):
        return "User name: {} {} ".format(self.name, self.alias)


class Friendship(models.Model):
    # Will result in a list of the friends for this user.
    from_friend = models.ForeignKey(User, related_name='friend_set')
    # Will result in a list of users who added this user as a friend.
    to_friend = models.ForeignKey(User, related_name='to_friend_set')


    def __unicode__(self):
        return u'%s, %s' % (self.from_friend.name, self.to_friend.name)

    class Meta:
        unique_together = (('to_friend', 'from_friend'),)