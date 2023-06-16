# Import libraries
from django.contrib import admin
from django.urls import path
from map import views as map_views

# define the url paths for exploring 
# different dfferent pages
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map_views.room, name='room'),
    path('home/',map_views.home, name='home'),
    path('contact/', map_views.contact, name='contact'),
    path('services/', map_views.services, name='services'),
    path('feedback/', map_views.feedback, name='feedback'),
    path('about/', map_views.about, name='about'),
    path('signup/', map_views.signup, name='signup'),
    path('activate/<uidb64>/<token>/', map_views.activate, name='activate'),
    path('signin/', map_views.signin, name='signin'),
    path('signout/', map_views.signout, name='signout'),
]
