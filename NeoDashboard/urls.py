from django.urls import path
from CustUserAuth.views import CustomLoginView, CustomLogoutView, ProfileView
from NeoDashboard.views import ChartView

urlpatterns = [
    path('chart/', ChartView.as_view(), name='chart'),

]
