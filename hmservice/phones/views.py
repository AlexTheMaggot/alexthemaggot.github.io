from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from phones.models import PhoneBrand, PhoneModel


class PhoneBrandListView(ListView):
    model = PhoneBrand
    template_name = "phones/brands.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PhoneModelListView(ListView):
    model = PhoneModel
    template_name = "phones/models.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
		
class PhoneModelDetailView(DetailView):

    model = PhoneModel
    template_name = "phones/model.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context