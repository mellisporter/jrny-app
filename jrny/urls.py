from django.contrib import admin  #allows us to use the admin side of the site
from django.urls import path, include # allows us to create paths and include in those paths

urlpatterns= [
    path('admin/' , admin.site.urls), #creates the admin url path for us
    path('', include('main_app.urls')), # creates the home/splash page
    path('accounts/' , include('django.contrib.auth.urls')), # allow users to be created
]
