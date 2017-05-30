from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
	COMPLETE = 'COMPLETE'
	NOT_STARTED = 'NOT_STARTED'
	IN_PROGRES = 'IN_PROGRES'

	TASK_CHOICES = (
		(COMPLETE, "Complete"),
		(NOT_STARTED, "Not Started"),
		(IN_PROGRES, "In Progres"),
	)

	LOW = 'LOW'
	NORMAL = 'NORMAL'
	HIGH = 'HIGH'

	PRIORITY_CHOICES  = (
		(LOW, "Low"),
		(NORMAL, "Normal"),
		(HIGH, "High"),
	)

	user = models.ForeignKey(User, related_name = 'user', default = None)
	host = models.CharField(max_length = 30, default = None, null = True)
	name = models.CharField(max_length = 60)
	description = models.CharField(max_length = 500)
	status = models.CharField(max_length=12, choices=TASK_CHOICES, default = NOT_STARTED)
	priority = models.CharField(max_length = 9, choices = PRIORITY_CHOICES, default = NORMAL)



	def __str__(self):
		return self.name