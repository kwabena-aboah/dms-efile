from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from efile.models import UserProfile
from efile.forms import PicForm

@login_required
def profile(request):
	"""Change user profile image"""
	if request.method != "POST":
		form = PicForm()
	else:
		form = PicForm(request.POST, request.FILES)
		if form.is_valid():
			picture = form.save(commit=False)
			picture.owner = request.user
			picture.save()
			messages.success(request, "Profile picture successfully updated")
	context = {'form':form}
	return render(request, 'inward/index.html', context)