from django.urls import path
from . import views

urlpatterns = [
    path('fetch-user-data/', views.fetch_user_data, name='fetch_user_data'),
    # ... other app-specific URL patterns ...
]
