from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('ViewBlog/',views.viewBlog),
    path('signup.html/',views.signup),
    path('display/<id>',views.click),
    path('PostBlog/', views.upload, name='imageupload'),
]
