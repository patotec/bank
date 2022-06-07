
from django.urls import path
from . import views
from .views import *
app_name='userurl'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginView, name='login'),
   
    path('logout/', views.logout_view, name='logout'),
   
    path('withdrawal/', views.withdrawal, name='withdraw'),
    path('deposit/', views.fund, name='depo'),
    path('pay-now/<slug>/', views.pay,name='pay'),
    path('otp/', views.otp,name='otp'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
   

    
]