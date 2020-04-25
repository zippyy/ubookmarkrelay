from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

from django.conf import settings

from ubookmark.models import *

class IndexView(ListView):
    model = BookmarkModel
    paginate_by = 3
    queryset = BookmarkModel.objects.order_by('-posted_at')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['site_name'] = settings.SITE_NAME
        context['site_description'] = settings.SITE_DESCRIPTION

        return context

class SubmitView(CreateView):
    model = BookmarkModel
    fields = [ 'comment', 'url' ]

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['site_name'] = settings.SITE_NAME
        context['site_description'] = settings.SITE_DESCRIPTION

        return context

class LoginView(auth_views.LoginView):
    pass
