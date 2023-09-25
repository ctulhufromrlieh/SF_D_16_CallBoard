# from datetime import datetime
from django_filters import FilterSet

from .models import Reply
import django_filters

class ReplyFilter(FilterSet):
    # post__title = django_filters.CharFilter(
    #     # field_name="post",
    #     lookup_expr="icontains",
    #     label="Заголовок",
    # ),

    class Meta:
        model = Reply
        fields = {
            "post__title": ['icontains']
        }
