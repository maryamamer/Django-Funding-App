"""FundingApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from users.views import Login, Registration, home, mylogout, profile, Update_Profile, userproject, activate
from projects.views import addproject, project, donate, cancel_project

from rest_framework import routers
from api.views import *
router=routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login),
    path('register', Registration),
    path('activate/<activeno>/', activate),
    path('home', home),
    path('logout', mylogout),
    path('profile', profile),
    path('UpdateProfile', Update_Profile),
    path('project', project, name="detail"),
    path('addproject', addproject),
    path('userproject', userproject),
    # path('project/<int:id>/comment', add_comment, name="add_comment"),
    path('donate/<int:id>', donate, name='donate'),
    path('cancel', cancel_project),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('projects/update/<int:id>', updateapi),
    path('projects/delete/<int:id>', deleteapiview),
    path('projects', projectlist),
    path('projects/add', createproject),
    path('projects/<int:id>', getproject),
]

from FundingApp import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
