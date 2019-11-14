from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from tablets.models import TabletBrand, TabletModel


class TabletBrandListView(ListView):

    model = TabletBrand
    template_name = 'tablets/brands.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        return context


class TabletModelListView(ListView):

    model = TabletModel
    template_name = 'tablets/models.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        return context

class TabletModelDetailView(DetailView):

    model = TabletModel
    template_name = 'tablets/model.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        return context