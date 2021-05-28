from django.urls import path
from django.urls.base import reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView, DetailView, delete_view

app_name = 'wiki'

urlpatterns = [
    path('auth/login/', auth_views.LoginView.as_view(), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', DetailView.as_view(), name='detail'),
    path('<slug:slug>/delete', delete_view, name='delete_page'),
    path('wiki/add/', views.create_view, name='page-add'),
    path('<slug:slug>/edit/', views.update_view, name='edit-view'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)