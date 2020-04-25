from django.views.generic.list import ListView

from ubookmark.models import *

class IndexView(ListView):

    model = BookmarkModel
    paginate_by = 50
