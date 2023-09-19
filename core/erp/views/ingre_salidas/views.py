from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.erp.models import IngresoSalida
from core.erp.forms import FormIngSal
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
class CreateViewIngSal(LoginRequiredMixin,CreateView):
    model = IngresoSalida
    form_class = FormIngSal
    template_name = 'ingre_salida/create.html'
    success_url = reverse_lazy('erp:ingsal_list')
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
        return JsonResponse({'datos':'datos'})
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Creacion de Ingreso y salidas'
        context['entidad'] = 'Ingreso y Salidas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
class ListViewIngSal(LoginRequiredMixin,ListView):
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
                    data.append(item)
            else:
                data['error'] = 'No se envio ninguna opcion'
        except Exception as e:
            data['error'] = f"Ocurrio un error {str(e)}" 
        return JsonResponse(data,safe=False)
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = "Ingresos y salidas"
        context['create_url'] = reverse_lazy('erp:ingsal_create')
        context['list_url'] = reverse_lazy('erp:ingsal_list')
        context['entidad'] = 'Ingresos Salidas'
        return context
class UpdateViewIngSal(LoginRequiredMixin,UpdateView):
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