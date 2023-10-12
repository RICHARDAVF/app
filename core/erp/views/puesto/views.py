
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.user.models import Puesto
from core.erp.forms import FormPuesto
from django.urls import reverse_lazy
from django.http import JsonResponse
class CreateViewPuesto(LoginRequiredMixin,CreateView):
    model = Puesto
    form_class = FormPuesto
    template_name = 'puesto/create.html'
    success_url = reverse_lazy('erp:puesto_list')
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
        context['title'] = "Creacion de un puesto"
        context['entidad'] = 'Puestos'
        context['list_url'] = self.success_url
        context['action'] = "add"
        return context
class ListViewPuesto(LoginRequiredMixin,ListView):
    model = Puesto
    template_name = 'puesto/list.html'
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Puesto.objects.select_related("unidad__empresa").filter(unidad_id=self.request.user.unidad_id)
        return Puesto.objects.select_related("unidad__empresa").all()
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = "Listado de Puestos"
        context['entidad'] = "Puestos"
        context['create_url'] = reverse_lazy('erp:puesto_create')
        return context
class DeleteViewPuesto(LoginRequiredMixin,DeleteView):
    model = Puesto
    success_url = reverse_lazy('erp:puesto_list')
    url_redirect = success_url
    template_name = 'puesto/delete.html'
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
        context['title'] = "Eliminacion de un puesto"
        context['entidad'] = 'Puestos'
        context['list_url'] = self.success_url
        return context
class UpdateViewPuesto(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Puesto
    form_class = FormPuesto
    template_name = 'puesto/create.html'
    success_url = reverse_lazy('erp:puesto_list')
    url_redirect = success_url
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                Puesto.objects.filter(id=kwargs['pk']).update(
                    unidad_id=request.POST['unidad'],
                    puesto=request.POST['puesto'],
                    direccion = request.POST['direccion']
                    )   
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Usuario'
        context['entidad'] = 'Usuarios'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context