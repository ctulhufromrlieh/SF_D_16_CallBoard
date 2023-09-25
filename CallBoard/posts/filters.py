# from datetime import datetime

from django import forms
from django_filters import FilterSet
# from django_filters.widgets import RangeWidget

from .models import Post, Category, Reply
import django_filters
import django.forms


# class DateTimeLocalInput(forms.DateTimeInput):
#     input_type = "datetime-local"


class ReplyFilter(FilterSet):
    # default_date_str = datetime.now().strftime("%Y-%m-%dT%H:%M")
    reply_title = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Заголовок",
    )
    categories = django_filters.ModelMultipleChoiceFilter(
        field_name="postcategory__category",
        queryset=Category.objects.all(),
        label="Категории:",
    )
    # creation_date = django_filters.DateTimeFilter(
    #     lookup_expr='gt',
    #     widget=DateTimeLocalInput(format="%Y-%m-%dT%H:%M"),
    #     label="Дата создания позднее чем:",
    # )

    class Meta:
        model = Reply
        fields = {
            # 'title': ['icontains'],
            # 'categories': ['exact'],
            # 'creation_date': ['gt'],
        }
