from django.views.generic.list import ListView

from laptops.models import LaptopBrand, LaptopModel


class LaptopBrandListView(ListView):

	model = LaptopBrand
	template_name = 'laptops/brands.html'

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		return context


class LaptopModelListView(ListView):

	model = LaptopModel
	template_name = 'laptops/models.html'

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		return context