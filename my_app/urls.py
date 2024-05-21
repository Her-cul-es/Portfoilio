from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('add_project/', views.add_project, name='add_project'),
    path('view_project/', views.view_project, name='view_project')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)