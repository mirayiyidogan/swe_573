from django.urls import path
from account.views import logout, reset_password, profile_update

urlpatterns = [
    path('logout', logout, name='logout'),
    path("reset-password", reset_password, name="reset-password"),
    # reset-password linkine karşılık reset_password view ı çalışarak url ismi de reset-password olacak
    path("profile-update", profile_update, name="profile-update"),
]