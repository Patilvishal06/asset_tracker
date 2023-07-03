"""Asset_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from AssetManagement.views import *

urlpatterns = [

    path('mange-asset-type/', MangeAssetTypeListView.as_view(), name='mange-asset-type-list'),
    path('mange-asset-type/create/', MangeAssetTypeCreateView.as_view(), name='mange-asset-type-create'),
    path('mange-asset-type/update/<int:pk>/', MangeAssetTypeUpdateView.as_view(), name='mange-asset-type-update'),
    path('mange-asset-type/delete/<int:pk>/', MangeAssetTypeDeleteView.as_view(), name='mange-asset-type-delete'),

    path('mange-asset/', MangeAssetListView.as_view(), name='mange-asset-list'),
    path('mange-asset/create/', MangeAssetCreateView.as_view(), name='mange-asset-create'),
    path('mange-asset/update/<int:pk>/', MangeAssetUpdateView.as_view(), name='mange-asset-update'),
    path('mange-asset/delete/<int:pk>/', MangeAssetDeleteView.as_view(), name='mange-asset-delete'),

]
