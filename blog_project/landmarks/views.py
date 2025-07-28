from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Landmark,Tag
from django.core.paginator import Paginator
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from .forms import CommentForm
# Create your views here. action = "{%url 'posts:search' %}" base.html
# "{% url 'posts:tag_posts' tag.id %}" for place.html
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

