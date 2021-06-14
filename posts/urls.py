from django.urls import path
from .views import (
    get_data,
    detail_data,
    create,
)


urlpatterns = [
    path('', get_data, name='index'),
    path('detail/<int:id>/', detail_data, name='detail_data'),
    path('create/', create, name='create_data')
]