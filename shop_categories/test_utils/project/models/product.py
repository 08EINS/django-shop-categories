from django.db import models
from tinymce import models as tinymce_models
from shop_categories.models.defaults.product.base import CategoryProductBase

class Product(CategoryProductBase):
    
    order = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = False
        app_label = 'project'