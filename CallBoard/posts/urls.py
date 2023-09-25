from django.urls import path

# from .views import PostList, PostCreate, PostUpdate, PostDelete, SearchedReplyList
from .views import PostList, PostCreate, PostUpdate, PostDelete, ReplyCreate, reply_accept_func


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('<int:post_id>/reply_create/', ReplyCreate.as_view(), name='reply_create'),
   path('replies/<int:reply_id>/reply_accept/', reply_accept_func, name='reply_accept'),
   # path('<int:post_id>/add_reply/', ReplyCreate.as_view(), name='reply_create'),
   # path('replies/', SearchedReplyList.as_view(), name='reply_list'),
   # path('', cache_page(60)(PostList.as_view()), name='post_list'),
   # path('search/', SearchedPostList.as_view()),
   # path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   # path('<int:pk>', cache_page(5*60)(PostDetail.as_view()), name='post_detail'),
   # path('create/', NewCreate.as_view(), name='new_create'),
   # path('<int:pk>/edit/', NewUpdate.as_view(), name='new_update'),
   # path('<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),
   # path('subscriptions/', subscriptions, name='subscriptions'),
]