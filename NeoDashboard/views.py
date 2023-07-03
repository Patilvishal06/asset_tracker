from django.shortcuts import render
from django.views.generic import TemplateView

from AssetManagement.models import MangeAssetTypeModel, ManageAssetModel


# Create your views here.

class ChartView(TemplateView):
    template_name = 'chartjs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get asset types for the pie chart
        asset_types = MangeAssetTypeModel.objects.all()
        context['asset_types'] = asset_types

        # Get the number of active and inactive assets for the bar chart
        active_assets = ManageAssetModel.objects.filter(is_active=True).count()
        inactive_assets = ManageAssetModel.objects.filter(is_active=False).count()
        context['active_assets'] = active_assets
        context['inactive_assets'] = inactive_assets

        return context
