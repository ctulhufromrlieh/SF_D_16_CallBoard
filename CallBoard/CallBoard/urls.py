"""
URL configuration for CallBoard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from ckeditor_uploader import views as ckeditor_views

from django.conf import settings
# from django.conf.urls import url, include
from posts.views import SearchedReplyList, ReplyDelete, reply_accept_func
# import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("allauth.urls")),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('ckeditor/', include('ckeditor.urls')),
    path('ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),
    path('posts/', include('posts.urls')),
    path('replies/', SearchedReplyList.as_view(), name='reply_list'),
    path('replies/<int:pk>/delete/', ReplyDelete.as_view(), name='reply_delete'),
    path('replies/<int:reply_id>/reply_accept/', reply_accept_func, name='reply_accept'),
    path('', RedirectView.as_view(url='posts/', permanent=False), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # serving media files only on debug mode
# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT
#         }),
#     ]