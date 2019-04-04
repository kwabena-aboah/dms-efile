from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from . models import Inward, InwardPic
from . forms import InwardForm, InwardPicForm
from efile.search import get_query

@login_required
def index(request):
    """ The homepage of eFile system"""
    return render(request, 'inward/index.html')


@login_required
def inward_list(request):
    """ List all inward entries """
    inwards = Inward.objects.filter(
        owner=request.user).order_by('date_received')
    paginator = Paginator(inwards, 25)  # show 25 inwards per page
    page = request.GET.get('page')
    inward = paginator.get_page(page)
    context = {"inwards": inwards, 'inward': inward}
    return render(request, 'inward/inward.html', context)


@login_required
def inward_detail(request, inward_id):
    detail = get_object_or_404(Inward, pk=inward_id)
    messages.info(request, "Inward successfully updated!")
    return HttpResponseRedirect('/inward_list/')


@login_required
def new_inward(request):
    """ Add new inward correspondence"""
    if request.method != 'POST':
        # blank form no data submitted
        form = InwardForm()
    else:
        # post submitted data / processed data
        form = InwardForm(request.POST)
        if form.is_valid():
            new_inward = form.save(commit=False)
            new_inward.owner = request.user
            new_inward.save()
            return HttpResponseRedirect(reverse('inward:inward_list'))
    context = {'form': form}
    return render(request, 'inward/new_inward.html', context)


@login_required
def edit_inward(request, inward_id):
    inward = Inward.objects.get(pk=inward_id)
    if request.method != 'POST':
        # prefill form with current inward
        form = InwardForm(instance=inward)
    else:
        # process data
        form = InwardForm(instance=inward, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('inward:inward_detail', args=[inward.id]))
    context = {'inward': inward, 'form': form}
    return render(request, 'inward/edit_inward.html', context)


@login_required
def delete_inward(request, inward_id):
    inward = Inward.objects.get(pk=inward_id)
    if inward.owner != request.user:
        raise Http404

    if inward:
        inward.delete()
        return HttpResponseRedirect(reverse('inward:inward_list'))
    return render(request, 'inward/inward.html')


@login_required
def list(request):
    """List uploaded images in a tabular form"""
    images = InwardPic.objects.filter(
        owner=request.user).order_by('created_on')
    paginator = Paginator(images, 10)  # show 10 inwards per page
    page = request.GET.get('page')
    image = paginator.get_page(page)
    context = {"images": images, 'image': image}
    return render(request, 'inward/list.html', context)


@login_required
def upload(request):
    """ handels image uploads form"""
    if request.method != "POST":
        form = InwardPicForm()
    else:
        form = InwardPicForm(request.POST, request.FILES)
        if form.is_valid():
            uploadImage = form.save(commit=False)
            uploadImage.owner = request.user
            uploadImage.save()
            return HttpResponseRedirect(reverse('inward:list'))
    context = {"form": form}
    return render(request, 'inward/upload.html', context)


@login_required
def search(request):
    query_string = ''
    found_inward = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        inward_query = get_query(query_string,
                    ['date_of_letter', 'date_received', 'received_from', 'ref_no', 'subject', 'officer_to', 'date_filed', 'file_number', 'owner'])
        found_inward = Inward.objects.filter(inward_query).order_by('-date_filed')
    context = {'query_string': query_string, 'found_inward': found_inward}
    return render(request, 'inward/inward.html', context)
