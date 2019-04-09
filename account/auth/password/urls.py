from django.urls import path
from . import views

urlpatterns = [
    path('/change', views.PasswordChange.as_view()),
    path('/change/done', views.PasswordChangeDone.as_view()),
    path('/reset', views.PasswordReset.as_view()),
    path('/reset/done', views.PasswordResetDone.as_view()),
    path('/reset/<uidb64>/<token>', views.PasswordResetConfirm.as_view()),
    path('/reset/done', views.PasswordResetComplete.as_view()),
]
