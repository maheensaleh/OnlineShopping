from . import views
from django.urls import path
from .views import FormDisplay,ConfirmAccount

urlpatterns = [
    path('user_form/', FormDisplay.as_view()),
    path('user_form/done/', ConfirmAccount.ok, name='ok')
]