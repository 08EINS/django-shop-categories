from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView
from shop.views.catalog import ProductRetrieveView
from shop_categories.models import Category


class CategoryShopListView(ListView):

    def get_queryset(self):
        category = get_object_or_404(Category, path=self.kwargs['path'])
        self.category = category
        queryset = super(CategoryShopListView, self).get_queryset()
        return queryset.filter(
            additional_categories__tree_id=category.tree_id,
            additional_categories__lft__gte=category.lft,
            additional_categories__rght__lte=category.rght
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super(CategoryShopListView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class CategoryProductDetailView(ProductRetrieveView):

    def get_queryset(self):
        queryset = super(CategoryProductDetailView, self).get_queryset()
        return queryset.filter(main_category__path=self.kwargs['path'])

    def get_context_data(self, **kwargs):
        context = super(
            CategoryProductDetailView, self).get_context_data(**kwargs)
        category = get_object_or_404(Category, path=self.kwargs['path'])
        context['category'] = category
        return context
