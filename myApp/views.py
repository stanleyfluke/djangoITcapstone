from django.shortcuts import render
from django.contrib.auth.models import User

def fetch_user_data(request):
    first_user = User.objects.first()
    
    user_data = {
        'userid': first_user.id,
        'username': first_user.username,
        
    }
    
    return render(request, 'user_data.html', {'user_data': user_data})