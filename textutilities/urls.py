"""
URL configuration for textutilities project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Importing functions, methods, class & other utilities from the file 'view.py' that we created
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # syntax: path('name_of_page', function_to_execute, name = 'The name to be shown')
    # name_of_page will be appended with http url: http://...../name_of_page
    # using our views file
    path('', views.index, name = 'Index'), # Index page aka Homepage which will execute codes from index()
    path('about/', views.about, name = 'About'),
    # path('ex/', views.ex, name = 'example'),  
    path('analyser', views.analyser, name='analyser')
]
