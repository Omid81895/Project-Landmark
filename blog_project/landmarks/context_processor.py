from .models import Tag
def categories(request):
    tags = Tag.objects.all()
    return{'tags': tags}