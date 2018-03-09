from __future__ import unicode_literals
from django.db import models

import re

valid_course_desc_regex = re.compile(r'[a-zA-Z ]{15,}')
valid_course_name_regex = re.compile(r'[a-zA-Z ]{5,}')


class CourseManager(models.Manager):
    def validate(self, post):
        messages = []

        if not valid_course_name_regex.match(post['course_name']):
            messages.append(
                {
                    "message": "Invalid name format! Must be at least 5 characters long.",
                    "message_tag": "course_name_validation"
                }
            )

        if not valid_course_desc_regex.match(post['course_description']):
            messages.append(
                {
                    "message": "Invalid description format! Must be at least 15 characters long.",
                    "message_tag":  "course_desc_validation"
                }
            )

        return messages


class Description(models.Model):
    description_field = models.CharField(max_length=255)

    def __str__(self):
        return "{} the description".format(self.description_field)


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return "{} the course".format(self.name)


class Comments(models.Model):
    comment_field = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, related_name="comments")

    def __str__(self):
        return "{} the course comment".format(self.comment_field)

