import uuid
from django.db import models

# Create your models here.

class MangeAssetTypeModel(models.Model):
    asset_type = models.TextField(blank= False , null = False ,unique = True)
    asset_description = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.asset_type


class ManageAssetModel(models.Model):
    asset_name = models.TextField(blank= False , null = False )
    asset_code = models.CharField(max_length=16, unique=True)
    asset_type = models.ForeignKey(MangeAssetTypeModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.asset_code:
            self.asset_code = str(uuid.uuid4().int)[:16]
        super().save(*args, **kwargs)

