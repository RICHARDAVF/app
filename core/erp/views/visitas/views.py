
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,View
from core.validation import Validation
from ...forms import FormVisitas,FormDelivery
from ...models import Salas,Parqueo,Visitas,Asistentes
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
import json
# Create your views here.
class CreateViewVisita(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Visitas
    form_class = FormVisitas
    template_name = 'visitas/create.html'
    success_url = reverse_lazy('erp:visita_list')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs) :
        data = {}
        try:
            action =request.POST['action']
            
            if action == "add":
                form = self.get_form()
                data = form.save()
                sala = request.POST['sala']
                if sala!='':
                    state_sale = Salas.objects.get(id=sala)
                    state_sale.estado = request.POST['estado']
                    state_sale.save()
                parqueo = request.POST['n_parqueo']
                if parqueo!='':
                    parking = Parqueo.objects.get(id=parqueo)
                    parking.estado = parqueo==''
                    parking.save()
               
            elif action =='searchdni':
                data = Validation(request.POST['dni']).valid()
               
            else:
                data['error'] = 'No se a ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)
    def get_form(self,form_class=None):
        form = super().get_form(form_class)
        form.fields['n_parqueo'].queryset=Parqueo.objects.filter(estado=True)
        form.fields['sala'].queryset=Salas.objects.filter(estado=0)
        return form
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
       
        context['title'] = 'Creacion de Visitas'
        context['entidad'] = 'Visitas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
class ListViewVisita(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Visitas
    template_name = 'visitas/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
   
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                try:
                    for value in Visitas.objects.all():
                        item = value.toJSON()
                        data.append(item)
                    
                except Exception as e:
                    data = {}
                    data['error'] = str(e)
            elif action =="addperson":
                try:
                    data = []
                    for index,value in  enumerate(Asistentes.objects.filter(visita_id=request.POST['id'])):
                        item = value.toJSON()
                        print(item)
                        data.append(item)
                except Exception as e:
                    data['error'] = f"Ocurrio un erro {str(e)}"
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
       
        return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Listado de Visitas'
        context['create_url'] = reverse_lazy('erp:visita_create')
        context['list_url'] = reverse_lazy('erp:visita_list')
        context['entidad'] = 'Visitas'
        return context
class UpdateViewVisita(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Visitas
    form_class = FormVisitas
    template_name = 'visitas/create.html'
    success_url = reverse_lazy('erp:visita_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
                if request.POST['h_termino']!='':
                    sala = request.POST['sala']
                    Salas.objects.filter(sala=sala).update(estado=0)
                    try:
                        Parqueo.objects.filter(numero=request.POST['n_parqueo']).update(estado=True)
                    except Exception as e:
                        pass
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['sala'].queryset = Salas.objects.filter(estado=0)
        visitas_instance = self.object
        sala_actual = visitas_instance.sala
        salas_estado_0 = Salas.objects.filter(estado=0)
        try:
            salas_combinadas = list(salas_estado_0) + [sala_actual]
            salas_queryset = Salas.objects.filter(Q(pk__in=[sala.pk for sala in salas_combinadas]))
            form.fields['sala'].queryset = salas_queryset
            form.fields['n_parqueo'].queryset = Parqueo.objects.filter(estado=True)
        except Exception as e:
            pass
        try:
            parqueo_actual = visitas_instance.n_parqueo
            parqueos_estado_true = Parqueo.objects.filter(estado=True)
            parqueos_combinados = list(parqueos_estado_true) + [parqueo_actual]
            parqueos_queryset = Parqueo.objects.filter(Q(pk__in=[parqueo.pk for parqueo in parqueos_combinados]))
            form.fields['n_parqueo'].queryset = parqueos_queryset
        except Exception as e:
            pass
       
        if self.request.method == 'GET':
            form.fields['sala'].initial = sala_actual
            form.fields['n_parqueo'].initial = parqueo_actual
       
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Visita'
        context['entidad'] = 'Visitas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
class DeleteViewVisita(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Visitas
    template_name = 'visitas/delete.html'
    success_url = reverse_lazy('erp:visita_list')
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
class CreateViewDelivery(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Visitas
    form_class = FormDelivery
    template_name = "delivery/create.html"
    success_url = reverse_lazy('erp:visita_list')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs) :
        data = {}
        try:
            action =request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            elif action =='searchdni':
                data = Validation(request.POST['dni']).valid()
               
            else:
                data['error'] = 'No se a ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)
    def get_form(self,form_class=None):
        form = super().get_form(form_class)
        return form
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
       
        context['title'] = 'Creacion de Visitas'
        context['entidad'] = 'Visitas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
class UpdateViewDelivery(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Visitas
    form_class = FormDelivery
    template_name = 'delivery/create.html'
    success_url = reverse_lazy('erp:visita_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

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
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Visita'
        context['entidad'] = 'Delivery'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context  
class CreateViewAsist(LoginRequiredMixin,View):
    login_url = reverse_lazy('login')
    model = Asistentes
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    def post(self,request,*ars,**kwargs):
        if request.POST['action'] == "addperson":
            print(request.POST)
            
            for item in json.loads(request.POST['items']):
                print(item)
                asis = Asistentes.objects.create(
                    visita_id=int(item["id"]),
                    documento=item['documento'],
                    nombre=item['nombre'],
                    apellidos = item['apellidos'],
                    empresa = item['empresa'],
                    marca_v=item['marca_v'],
                    modelo_v=item['modelo_v'],
                    placa_v=item['placa_v'],
                    soat_v=item['soat_v'],
                    strc=item['strc'],
                    n_parqueo_id=item['n_parqueo'],
                )
                asis.save()
        return JsonResponse({"success":"Success"})
    