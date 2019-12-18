from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.fields import JSONField
import json
from datetime import datetime
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.data import JsonLexer


class Profile(models.Model):
    STUDENT = 'Student'
    COLLEGEADMIN = 'College-admin'
    ADMIN = 'Admin'
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (COLLEGEADMIN, 'College-admin'),
        (ADMIN, 'Admin'),
    )
    ADMIN = 'Admin'
    NARAYANA = 'Narayana'
    CHAITHANYA = 'Chaithanya'
    SCHOOL_NAME = (
    	(ADMIN,'Admin'),
    	(NARAYANA,'Narayana'),
    	(CHAITHANYA,'Chaithanya'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=256, choices=SCHOOL_NAME,null=True, blank=True)
    role = models.CharField(max_length=256, choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
class Narayana_Question(models.Model):
	question = models.TextField()
	option1 = models.CharField(max_length=300)
	option2 = models.CharField(max_length=300)
	option3 = models.CharField(max_length=300)
	option4 = models.CharField(max_length=300)
	correct_option = models.CharField(max_length=300)
	accuracy_count = models.DecimalField(default=0,max_digits=100,decimal_places=0)

class Chaithanya_Question(models.Model):
	question = models.TextField()
	option1 = models.CharField(max_length=300)
	option2 = models.CharField(max_length=300)
	option3 = models.CharField(max_length=300)
	option4 = models.CharField(max_length=300)
	correct_option = models.CharField(max_length=300)
	accuracy_count = models.DecimalField(default=0,max_digits=100,decimal_places=0)

class Narayana_Submission(models.Model):
    name = models.TextField()
    data = JSONField()
    score = models.IntegerField()
    time = models.IntegerField()
    created = models.DateTimeField(default=datetime.now)
    def detail_nar_json_formatted(self):
        data = json.dumps(self.data, indent=2)
        formatter = HtmlFormatter(style='colorful')
        response = highlight(data, JsonLexer(), formatter)
        style = "<style>" + formatter.get_style_defs() + "</style><br/>"
        return mark_safe(style + response)
    detail_nar_json_formatted.short_description = 'Details Formatted'
    class Meta:
        managed = True

class Chaithanya_Submission(models.Model):
    name = models.TextField()
    data = JSONField()
    score = models.IntegerField()
    time = models.IntegerField()
    created = models.DateTimeField(default=datetime.now)
    def detail_chai_json_formatted(self):
        data = json.dumps(self.data, indent=2)
        formatter = HtmlFormatter(style='colorful')
        response = highlight(data, JsonLexer(), formatter)
        style = "<style>" + formatter.get_style_defs() + "</style><br/>"
        return mark_safe(style + response)
    detail_chai_json_formatted.short_description = 'Details Formatted'
    class Meta:
        managed = True