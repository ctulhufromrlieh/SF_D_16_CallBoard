from django.urls import path

# from .views import PostList, PostCreate, PostUpdate, PostDelete, SearchedReplyList
from .views import PostList, PostCreate, PostUpdate, PostDelete, ReplyCreate, reply_accept_func


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   # path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('<int:post_id>/reply_create/', ReplyCreate.as_view(), name='reply_create'),
]