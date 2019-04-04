from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from . models import Outward, OutwardPic 
from . forms import OutwardForm, OutwardPicForm


@login_required
def outward_list(request):
	""" List all outward entries """
	outwards = Outward.objects.filter(owner=request.user).order_by('date_received')
	paginator = Paginator(outwards, 25)	# show 25 outwards per page
	page = request.GET.get('page')
	outward = paginator.get_page(page)
	context = {"outwards": outwards, 'outward':outward}
	return render(request, 'outward/outward.html', context)

@login_required
def outward_detail(request, outward_id):
	detail = get_object_or_404(Outward,pk=outward_id)
	messages.info(request, "Outward successfully updated!")
	return HttpResponseRedirect(reverse('outward:outward_list'))

@login_required
def new_outward(request):
	""" Add new outward correspondence"""
	if request.method != 'POST':
		# blank form no data submitted
		form = OutwardForm()
	else:
		# post submitted data / processed data
		form = OutwardForm(request.POST)
		if form.is_valid():
			new_outward = form.save(commit=False)
			new_outward.owner = request.user
			new_outward.save()
			return HttpResponseRedirect(reverse('outward:outward_list'))
	context = {'form':form}
	return render(request, 'outward/new_outward.html', context)


@login_required
def edit_outward(request, outward_id):
	outward = Outward.objects.get(pk=outward_id)
	if request.method != 'POST':
		# prefill form with current outward
		form = OutwardForm(instance = outward)
	else:
		# process data
		form = OutwardForm(instance=outward, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('outward:outward_detail', args=[outward.id]))
	context = {'outward':outward, 'form':form}
	return render(request, 'outward/edit_outward.html', context)


@login_required
def delete_outward(request, outward_id):
	outward = Outward.objects.get(pk=outward_id)
	if outward.owner != request.user:
		raise Http404

	if outward:
		outward.delete()
		return HttpResponseRedirect(reverse('outward:outward_list'))
	return render(request, 'outward/outward.html')

@login_required
def list(request):
	"""List uploaded images in a tabular form"""
	images = OutwardPic.objects.filter(owner=request.user).order_by('created_on')
	paginator = Paginator(images, 10)	# show 10 outwards per page
	page = request.GET.get('page')
	image = paginator.get_page(page)
	context = {"images":images, 'image':image}
	return render(request, 'outward/list.html', context)

@login_required
def upload(request):
	""" handels image uploads form"""
	if request.method != "POST":
		form = OutwardPicForm()
	else:
		form = OutwardPicForm(request.POST, request.FILES)
		if form.is_valid():
			uploadImage = form.save(commit=False)
			uploadImage.owner = request.user
			uploadImage.save()
			return HttpResponseRedirect(reverse('outward:list'))
	context = {"form":form}
	return render(request, 'outward/upload.html', context)