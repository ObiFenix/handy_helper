# =====================================
# Required imported modules and classes
# =====================================
from __future__ import unicode_literals
from django.db import models
from ..accounts.models import User
# from datetime import datetime
# import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# =========================
# Required CustomValidation
# =========================
class JobManager(models.Manager):

    def jobValidator(self, postData):
        errors = {}
        if (len(postData['title'])       < 1):  errors['isemptyfield'] = "These fields cannot be blank."
        if (len(postData['description']) < 1):  errors['isemptyfield'] = "These fields cannot be blank."
        if (len(postData['location'])    < 1):  errors['isemptyfield'] = "These fields cannot be blank."
        return errors



# ================================
# Required Models for thsis Projec
# ================================
class Job(models.Model):
    title      = models.CharField(max_length = 255)
    desc       = models.CharField(max_length = 255)
    location   = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now = True)
    creator    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs_created')
    users_jobs = models.ManyToManyField(User, related_name='myjobs')
    objects    = JobManager()

    # Formatting Data Display
    def __str__(self):
        report  = "\n\nTitle: {}\nDescription: {}\n".format(self.title, self.desc)
        return report
