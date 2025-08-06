from .models import Tag, PickTheme
def categories(request):
    tags = Tag.objects.all()
    return{'tags': tags}

def theme(request):
    if request.user.is_authenticated:
        _picktheme = PickTheme.objects.filter(user=request.user).last()
    
    else:
        _picktheme = None
            
    return {
        'user_pref': _picktheme,
        'theme': request.COOKIES.get('theme', 'light')
    }