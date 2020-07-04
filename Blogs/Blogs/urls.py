"""Blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from usermanagement.custom_jwt import MyTokenObtainPairView
from usermanagement.views import *
from blogsmanagement.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-user/', SignUpManagement.as_view()),
    path('login/', MyTokenObtainPairView.as_view(), name='token'),
    path('get-user-info/', GetUserInfo.as_view()),
    path('dashboard/create-article/', CreateArticle.as_view()),
    path('dashboard/update-article/', UpdateArticle.as_view()),
    path('dashboard/get-blogs/', GetBlogs.as_view()),
    path('dashboard/article-by-id/<int:id>/', GetArticleById.as_view()),
    path('get-blogs/<int:id>/', GetApprovedArticleById.as_view()),
    path('get-blogs/', GetALlApprovedArticles.as_view())
]
