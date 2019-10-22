#by me

from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.Help ,name="Help"),
    path('Help_confrm/',views.Help_confrm,name="Help_confrm")
    ]
