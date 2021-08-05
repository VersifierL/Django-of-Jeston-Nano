# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.forms import MomentForm
from django.urls import reverse
import os
def moments_input(request):
	if request.method == 'POST':
		form = MomentForm(request.POST)
		if form.is_vaild():
			moment = form.save()
			moment.save()
			return HttpResponseRedirect(reverse("app.views.welcome"))
	else:
		form = MomentForm()
	PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	return render(request, os.path.join(PROJECT_ROOT, 'app/templates', 'moments_input.html'), {'form': form})

