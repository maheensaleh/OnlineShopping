#by me

from . import views
from django.urls import path

urlpatterns = [
    path('',views.mobile,name="mobile"),
    path('Samsung/',views.Samsung,name="Samsung"),
    path('Nokia/',views.Nokia,name="Nokia"),
    path('Apple/',views.Apple,name="Apple"),
]
