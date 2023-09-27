from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

from .models import Post, Reply
from .forms import PostForm, ReplyForm
from .filters import ReplyFilter



# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-id'
    # ordering = '-creation_date'

    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    # def get_is_editables(user):
    #     Post.objects

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['current_user'] = self.request.user
    #     # context['is_editables'] = get_is_editables(self.request.user)
    #     # context['current_time'] = timezone.now()
    #     # context['timezones'] = pytz.common_timezones
    #     return context

    # def post(self, request):
    #     request.session['django_timezone'] = request.POST['timezone']
    #     # return redirect('/')
    #     return redirect(request.get_full_path())


# class PostCreate(PermissionRequiredMixin, CreateView):
class PostCreate(LoginRequiredMixin, CreateView):
    # permission_required = ('posts.add_post',)
    form_class = PostForm
    model = Post
    # template_name = 'post_edit.html'
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

    # def get_form_kwargs(self):
    #     kw = super(PostCreate, self).get_form_kwargs()
    #     kw['user'] = self.request.user # the trick!
    #     return kw

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)


# class NewUpdate(PermissionRequiredMixin, UpdateView):
#     permission_required = ('news.change_post',)
class PostUpdate(UserPassesTestMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        the_object = self.get_object()
        return the_object.author.id == self.request.user.id

    # def get_form_kwargs(self):
    #     kw = super(PostUpdate, self).get_form_kwargs()
    #     kw['user'] = self.request.user # the trick!
    #     return kw

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)


# class NewDelete(PermissionRequiredMixin, DeleteView):
#     permission_required = ('news.delete_post',)
class PostDelete(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        the_object = self.get_object()
        return the_object.author.id == self.request.user.id


class SearchedReplyList(LoginRequiredMixin, ListView):
    model = Reply
    ordering = '-id'
    template_name = 'replies_search.html'
    context_object_name = 'replies'
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        queryset = queryset.filter(post__author__id=self.request.user.id)

        self.filterset = ReplyFilter(self.request.GET, queryset)
        return self.filterset.qs
        # return self.filterset.qs.filter(user=)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset

        return context


class ReplyCreate(UserPassesTestMixin, CreateView):
    form_class = ReplyForm
    model = Reply
    template_name = 'reply_create.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        # post_id = self.kwargs.pop('post_id', None)
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)

        return not post.author.id == self.request.user.id

    def form_valid(self, form):
        post_id = self.kwargs.pop('post_id', None)

        self.object = form.save(commit=False)
        self.object.post = Post.objects.get(id=post_id)
        self.object.user = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)


class ReplyDelete(UserPassesTestMixin, DeleteView):
    model = Reply
    template_name = 'reply_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        the_object = self.get_object()
        return the_object.post.author.id == self.request.user.id


# def reply_accept_test_func(request):
def is_allowed_reply_accept(user, reply):
    if reply.is_accepted:
        return False
    if user.is_authenticated:
        return not user.id == reply.user.id


# @login_required
@csrf_protect
def reply_accept_func(request, reply_id):
    if request.method == 'POST':
        # reply_id = request.POST.get('reply_id')
        reply = Reply.objects.get(id=reply_id)

        if not is_allowed_reply_accept(request.user, reply):
            raise PermissionDenied

        reply.accept()
        reply.save()

    path_to_return = request.POST.get('next', '/')
    return HttpResponseRedirect(path_to_return)
