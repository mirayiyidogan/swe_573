from django.urls import path
from account.views import logout, reset_password, profile_update, registration, ProfileDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name = 'pages/login.html'
    ), name='login'),
    path('logout', logout, name='logout'),
    path("reset-password", reset_password, name="reset-password"),
    # reset-password linkine karşılık reset_password view ı çalışarak url ismi de reset-password olacak
    path("profile-update", profile_update, name="profile-update"),
    path("registration", registration, name="registration"),
    path("user/<str:username>", ProfileDetailView.as_view(), name="profile"),

]