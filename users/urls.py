from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    #clothes views
    path('register', views.register, name="register"),
    path('profile/<str:username>', views.profile, name="profile"),
    path('sign_in_action', views.login_user, name="sign_in"),
    path('log_out/', views.logout_user, name="log_out"),
]