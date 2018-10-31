# =====================================
# Required imported modules and classes
# =====================================
from __future__ import unicode_literals
from django.db import models
# from datetime import datetime
# import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# =========================
# Required CustomValidation
# =========================
class UserManager(models.Manager):

    def registerValitator(self,postData):
        errors = {}
        _firsname  = postData['first_name']
        _lastname  = postData['last_name']
        _email     = postData['email']
        _password  = postData['password']
        _confirmpw = postData['confirm_pw']
        if len(_firsname) < 2 or not str.isalpha(_firsname):  errors['first_name'] = 'First name must be at least 2 charachters long and contain no numbers.'
        if len(_lastname) < 2 or not str.isalpha(_lastname):  errors['last_name'] = 'Last name must be at least 2 charachters long and contain no numbers.'
        if len(_email) < 1 or not EMAIL_REGEX.match(_email):  errors['email'] = 'Must enter a valid email address!'
        if len(_password) < 5:                                errors['password'] = 'Pasword must be at least 5 charachters!'
        if _confirmpw != _password:                           errors['confirm_pw'] = 'Your passwords do not match!'
        return errors

    def updateValitator(self,postData):
        errors = {}
        _firsname  = postData['first_name']
        _lastname  = postData['last_name']
        _email     = postData['email']
        if len(_firsname) < 2 or not str.isalpha(_firsname):  errors['first_name'] = 'First name must be at least 2 charachters long and contain no numbers.'
        if len(_lastname) < 2 or not str.isalpha(_lastname):  errors['last_name'] = 'Last name must be at least 2 charachters long and contain no numbers.'
        if len(_email) < 1 or not EMAIL_REGEX.match(_email):  errors['email'] = 'Must enter a valid email address!'
        return errors

    def loginValitator(self, postData):
        errors = {}
        _loginemail = postData['login_email']
        _password   = postData['password']
        if len(_loginemail) < 1 or len(_password) < 5 or not EMAIL_REGEX.match(_loginemail):  errors['login_email'] = 'Must enter a valid login email and password!'
        # if len(_password) < 5:                                          errors['password'] = 'Please verify your password!'
        return errors

    def jobValidator(self, postData):
        errors = {}
        if (len(postData['title'])       < 1):  errors['isemptyfield'] = "These fields cannot be blank."
        if (len(postData['description']) < 1):  errors['isemptyfield'] = "These fields cannot be blank."
        if (len(postData['location'])    < 1):  errors['isemptyfield'] = "These fields cannot be blank."
        return errors

# ================================
# Required Models for thsis Projec
# ================================
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name  = models.CharField(max_length = 255)
    email      = models.CharField(max_length = 255,unique=True)
    password   = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects    = UserManager()

    # Formatting Data Display
    def __str__(self):
        report  = "\n\nFirst Name: {}\nLast Name : {}\nEmail     : {}\n".format(self.first_name, self.last_name, self.email)
        return report
