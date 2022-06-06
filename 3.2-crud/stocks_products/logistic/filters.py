import django_filters

from logistic.models import Product, Stock


class StockFilter(django_filters.FilterSet):
    products = django_filters.CharFilter(
        field_name='products__title',
        lookup_expr='icontains',
    )

    class Meta:
        model = Stock
        fields = ('products',)

