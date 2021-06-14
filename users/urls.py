from django.urls import path
from .views import profile


urlpatterns = [
    path('<int:id>/', profile, name='profile')
]