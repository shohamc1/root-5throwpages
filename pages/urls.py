from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path('', views.page, name='page'),
    path('submit', views.upload, name='upload'),
]