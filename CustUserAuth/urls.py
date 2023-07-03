from django.urls import path
from CustUserAuth.views import CustomLoginView, CustomLogoutView, ProfileView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),

]
