from django.views.generic.list import ListView

from cameras.models import CameraBrand, CameraModel


class CameraBrandListView(ListView):
    model = CameraBrand
    template_name = "cameras/brands.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CameraModelListView(ListView):
    model = CameraModel
    template_name = "cameras/models.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
		