from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.conf import settings

from ubookmark.models import *

class IndexView(ListView):
    model = BookmarkModel
    paginate_by = 5
    queryset = BookmarkModel.objects.order_by('-posted_at')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['site_name'] = settings.SITE_NAME
        context['site_description'] = settings.SITE_DESCRIPTION
        context['site_description'] = settings.SITE_DESCRIPTION

        return context

class SubmitView(LoginRequiredMixin, CreateView):
    model = BookmarkModel
    fields = [ 'comment', 'url' ]
    login_url = '/login/'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['site_name'] = settings.SITE_NAME
        context['site_description'] = settings.SITE_DESCRIPTION

        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(SubmitView, self).form_valid(form)

class LoginView(auth_views.LoginView):
    template_name = 'ubookmark/login.html'
    extra_context = {}

    extra_context['site_name'] = settings.SITE_NAME
    extra_context['site_description'] = settings.SITE_DESCRIPTION


def logout_view(request):
    logout(request)
    return redirect("/")
