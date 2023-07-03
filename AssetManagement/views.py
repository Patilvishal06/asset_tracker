from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MangeAssetTypeModel, ManageAssetModel


# List view to display all objects
class MangeAssetTypeListView(ListView):
    model = MangeAssetTypeModel
    template_name = 'datatable.html'  # Replace with your actual template name
    context_object_name = 'asset_types'  # Replace with the context variable name you prefer

# Create view to create a new object
class MangeAssetTypeCreateView(CreateView):
    model = MangeAssetTypeModel
    template_name = 'MangeAssetTypeModel_create.html'  # Replace with your actual template name
    fields = '__all__'  # Replace with the fields you want to include in the form
    success_url = reverse_lazy('mange-asset-type-list')  # Replace with the URL name of the list view

# Update view to update an existing object
class MangeAssetTypeUpdateView(UpdateView):
    model = MangeAssetTypeModel
    template_name = 'MangeAssetTypeModel_update.html'  # Replace with your actual template name
    fields = '__all__'  # Replace with the fields you want to include in the form
    success_url = reverse_lazy('mange-asset-type-list')  # Replace with the URL name of the list view

# Delete view to delete an object
class MangeAssetTypeDeleteView(DeleteView):
    model = MangeAssetTypeModel
    template_name = 'MangeAssetTypeModel_confirm_delete.html'  # Replace with your actual template name
    success_url = reverse_lazy('mange-asset-type-list')  # Replace with the URL name of the list view


# List view to display all objects
class MangeAssetListView(ListView):
    model = ManageAssetModel
    template_name = 'datatable_manage_asset.html'  # Replace with your actual template name
    context_object_name = 'manage_asset'  # Replace with the context variable name you prefer

# Create view to create a new object
class MangeAssetCreateView(CreateView):
    model = ManageAssetModel
    template_name = 'MangeAssetModel_create.html'  # Replace with your actual template name
    fields = ['asset_name' , 'asset_type' , 'is_active']  # Replace with the fields you want to include in the form
    success_url = reverse_lazy('mange-asset-list')  # Replace with the URL name of the list view

# Update view to update an existing object
class MangeAssetUpdateView(UpdateView):
    model = ManageAssetModel
    template_name = 'MangeAssetModel_update.html'  # Replace with your actual template name
    fields = '__all__'  # Replace with the fields you want to include in the form
    success_url = reverse_lazy('mange-asset-list')  # Replace with the URL name of the list view

# Delete view to delete an object
class MangeAssetDeleteView(DeleteView):
    model = ManageAssetModel
    template_name = 'MangeAssetModel_confirm_delete.html'  # Replace with your actual template name
    success_url = reverse_lazy('mange-asset-list')  # Replace with the URL name of the list view


