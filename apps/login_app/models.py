from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import datetime
# Create your models here.
class UserManager(models.Manager):
    def RegVal(self, PostData):
        results = {'status': True, 'errors': []}
        if len(PostData['name']) < 3:
            results['errors'].append('Your name is too short')
        if PostData['name'].isspace() == True:
            results['errors'].append('Cant have just spaces ray!')
        if len(PostData['alias']) < 3:
            results['errors'].append('Your name is too short')
        if PostData['alias'].isalpha() == False:
            results['errors'].append('Cant have just spaces ray!')
        if not re.match('(\w+[.|\w])*@(\w+[.])*\w+', PostData['email']):
            results['errors'].append('enter valid email')
        if len(PostData['password']) < 5:
            results['errors'].append('Your password is too short')
        if PostData['password'] != PostData['c_password']:
            results['errors'].append('Your passwords must match')
        if len(self.filter(email=PostData['email'])) > 0:
            results['errors'].append('User already exists')
        if len(results['errors']) > 0:
            results['status'] = False
        return results
    def creator(self, PostData):
        hashed  = bcrypt.hashpw(PostData['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name = PostData['name'], alias = PostData['alias'], email = PostData['email'], password = hashed, birthdate=PostData['birthdate'])
        return user
    def logVal(self, PostData):
        results = {'status': True, 'errors': [], 'user': None}
        users = self.filter(email = PostData['email'])
        if len(users) < 1:
            results['errors'].append('No user with that email')
        else:
            if bcrypt.checkpw(PostData['password'].encode(), users[0].password.encode()) == False:
                results['errors'].append('incorrect password')
        if len(results['errors']) > 0:
            results['status'] = False
        else:
            results['user'] = users[0]   
        return results    
        
class User(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthdate = models.DateField(default=12/27/1989)
    friend_id = models.ManyToManyField('self', related_name="friendlist")
    objects = UserManager()
