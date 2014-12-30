from django.shortcuts import render

from django.contrib.auth import get_user_model
User = get_user_model()

def index(request):
    try:
        you = User.objects.get(pk=1)
    except User.DoesNotExist:
        you = {}
    
    return render(request, 'index.html', {'you': you})