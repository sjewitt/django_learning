"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path

'''
note that I am importing the APP (poll) into the PROJECT (test1)
'''
urlpatterns = [
    # this sets the root of the APP: It is a subdirectory of the project.
    # TODO: Check out non-sibling app code as per note in tutorial.
    path('polls/', include('polls.urls')),

     #so I can use index as default too
    path('polls/index', include('polls.urls')),

    # for admin functions - behind an auth wall
    path('admin/', admin.site.urls)
]
