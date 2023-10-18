from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import PermisosMixins
from core.erp.models import IngresoSalida
from core.erp.forms import FormIngSal
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class CreateViewIng(LoginRequiredMixin,PermisosMixins,CreateView):
    permission_required = 'erp.add_ingresosalida'
    model = IngresoSalida
    form_class = FormIngSal
    template_name = 'ingre_salida/create.html'
    success_url = reverse_lazy('erp:ing_create')
    url_redirect = success_url
    def post(self, request, *args, **kwargs) :
        data = {}
        try:
            action = request.POST['action']
            
            if action =='add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "no se envio ninguna opcion"
        except Exception as e:
            data['error'] = f"Ocurrio un error: "
        return JsonResponse(data)
    def get_form(self, form_class=None):
        form =  super().get_form(form_class)
        form.fields['tipo'].initial = "1"
        return form
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Creacion de un Ingreso'
        context['entidad'] = 'Ingresos'
        context['action'] = 'add'
        return context
class CreateViewSal(LoginRequiredMixin,PermisosMixins,CreateView):
    permission_required = 'erp.add_ingresosalida'
    model = IngresoSalida
    form_class = FormIngSal
    template_name = 'ingre_salida/create.html'
    success_url = reverse_lazy('erp:sal_create')
    url_redirect = success_url
    def post(self, request, *args, **kwargs) :
        data = {}
        try:
            action = request.POST['action']
            if action =='add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "no se envio ninguna opcion"
        except Exception as e:
            data['error'] = f"Ocurrio un error: {str(e)}"
        return JsonResponse(data)
    def get_form(self, form_class=None):
        form =  super().get_form(form_class)
        form.fields['tipo'].initial = "2"
        return form
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Creacion de un Salida '
        context['entidad'] = 'Salidas'
        context['action'] = 'add'
        return context
class ListViewIngSal(LoginRequiredMixin,PermisosMixins,ListView):
    permission_required = 'erp.view_ingresosalida'
    login_url = reverse_lazy('login')
    model = IngresoSalida
    template_name = 'ingre_salida/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action =="searchdata":
                data = []
                for value in IngresoSalida.objects.all():
                  
                    item = value.toJSON()
                    item['fecha'] = value.fecha
                    item['hora'] = value.hora.strftime('%H:%M:%S')
                    data.append(item)
            else:
                data['error'] = 'No se envio ninguna opcion'
        except Exception as e:
            data['error'] = f"Ocurrio un error {str(e)}" 
        return JsonResponse(data,safe=False)
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de ingresos y salidas"
        context['list_url'] = reverse_lazy('erp:ingsal_list')
        context['entidad'] = 'Salidas'
        return context
class UpdateViewIngSal(LoginRequiredMixin,PermisosMixins,UpdateView):
    permission_required = 'erp.change_ingresosalida'
    login_url = reverse_lazy('login')
    model = IngresoSalida
    form_class = FormIngSal
    template_name = 'ingre_salida/create.html'
    success_url = reverse_lazy('erp:ingsal_list')
    url_redirect = success_url
    def dispatch(self,request,*args,**kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No se ingreso ninguna opcion"
        except Exception as e:
            data['error'] = f"Ocurrio un erro: {str(e)}"
        return JsonResponse(data)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de un Ingreso O salida"
        context['entidad'] = "Ingresos y Salidas"
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context  
class DeleteViewIngSal(LoginRequiredMixin,PermisosMixins,DeleteView):
    permission_required = 'erp.delete_ingresosalida'
    login_url = reverse_lazy('login')
    model = IngresoSalida
    template_name = 'ingre_salida/delete.html'
    success_url = reverse_lazy('erp:ingsal_list')
    url_redirect = success_url


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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Visita'
        context['Entidad'] = 'Visitas'
        context['list_url'] = self.success_url
        return context