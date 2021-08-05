# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
KIND_CHOICES = (
	('Chinese', 'Chinese'),
	('Math', 'Math'),
	('English', 'English'),
)

class Moment(models.Model):
	content = models.CharField(max_length=300)
	user_name = models.CharField(max_length = 20)
	# 修改kind定义，加入choices参数
	kind = models.CharField(max_length = 20, choices = KIND_CHOICES, default = KIND_CHOICES[0])

