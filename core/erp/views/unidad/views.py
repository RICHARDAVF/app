from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from core.user.models import Unidad
from core.erp.forms import FormUnidad
from django.urls import reverse_lazy
from django.http import JsonResponse

class CreateViewUnidad(LoginRequiredMixin,CreateView):
    model = Unidad
    form_class = FormUnidad
    template_name = 'unidad/create.html'
    success_url = reverse_lazy('erp:unidad_list')
    # permission_required = 'erp.view_unidad'
    # permission_denied_message = 'Usted no tiene acceso a esta vista'
    # login_url = None
    def post(self, request, *args, **kwargs) :
        data = {}
        try:
            action = request.POST['action']
            if action =='add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No se ingreso ninguna opcion"
        except Exception as e:
            data['error'] = f"Ocurrio un error: {str(e)}"
        return JsonResponse(data,safe=False)
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['title'] = "Creacion de una unidad"
        context['entidad'] = 'Unidad'
        context['list_url'] = self.success_url
        context['action'] = "add"
        return context
class ListViewUnidad(LoginRequiredMixin,ListView):
    model = Unidad
    template_name = 'unidad/list.html'
    def get_queryset(self):
        return Unidad.objects.select_related("empresa").all()
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = "Listado de Unidades"
        context['entidad'] = "Unidades"
        context['create_url'] = reverse_lazy('erp:unidad_create')
        return context
class DeleteViewUnidad(LoginRequiredMixin,DeleteView):
    model = Unidad
    success_url = reverse_lazy('erp:unidad_list')
    url_redirect = success_url
    template_name = 'unidad/delete.html'
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = "Eliminacion de una unidad"
        context['entidad'] = 'Unidades'
        context['list_url'] = self.success_url
        return context
class UpdateViewUnidad(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Unidad
    form_class = FormUnidad
    template_name = 'unidad/create.html'
    success_url = reverse_lazy('erp:unidad_list')
    url_redirect = success_url
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Unidad'
        context['entidad'] = 'Unidades'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context