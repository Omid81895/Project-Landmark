from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Landmark,Tag
from django.core.paginator import Paginator
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from .forms import CommentForm, LandmarkForm
from django.db.models import Q
# Create your views here. action = "{%url 'posts:search' %}" base.html
def home(request):
    page_number = request.GET.get('page', 1)
    landmarks = Landmark.objects.all().order_by('id')
    paginator = Paginator(landmarks, 3)
    page_obj = paginator.get_page(page_number)
    return TemplateResponse(request, 'landmarks/home.html', {'landmarks': page_obj, 'paginator': paginator})

def landmark(request,id):
    requested_landmark = get_object_or_404(Landmark, id=id)
    comments = requested_landmark.comments.all()
    tags = requested_landmark.tag.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.landmark = requested_landmark
            comment.user = request.user
            comment.save()
            url = reverse('single_place', args=[id])
            return redirect(url)
    else:
        form = CommentForm()
    return render(request, 'landmarks/place.html', context={
                                                            'landmark': requested_landmark,
                                                            'form': form,
                                                            'comments': comments,
                                                            'tags': tags
                                                            })
def add(request):
    if request.method == 'POST':
        form = LandmarkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'landmarks/add.html', {'form': form})
    else:
        form = LandmarkForm()
    return render(request, 'landmarks/add.html', {'form': form})
def filter_read(request, id):
    tag = Tag.objects.get(id=id)
    landmarks = tag.landmark_set.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(landmarks, 3)
    page_obj = paginator.get_page(page_number)
    return render(request, 'landmarks/filter.html', {'landmarks': page_obj, 'paginator': paginator})

def search(request):
    query = request.GET['query']
    landmarks = Landmark.objects.filter(Q(name__icontains = query)|Q(description__icontains = query))
    page_number = request.GET.get('page', 1)
    paginator = Paginator(landmarks, 3)
    page_obj = paginator.get_page(page_number)
    return render(request, 'landmarks/filter.html', {'landmarks': page_obj, 'paginator': paginator})

