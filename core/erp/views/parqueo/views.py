from typing import Any, Dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from ...models import Parqueo
from ...forms import FormParqueo
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class CreateViewParqueo(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Parqueo
    form_class = FormParqueo
    template_name = 'parqueo/create.html'
    success_url = reverse_lazy('erp:parqueo_list')
    def post(self, request, *args, **kwargs) :
        data = {}
        try:
            action =request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No se a ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = 'Creacion de una Parqueo'
        context['entidad'] = 'Parqueos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
class ListViewParqueo(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Parqueo
    template_name = 'parqueo/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
       
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                if not request.user.is_superuser:
                    for value in Parqueo.objects.filter(empresa_id=request.user.empresa_id,unidad_id=request.user.unidad_id,puesto_id=request.user.puesto_id):
                        item = value.toJSON()
                        data.append(item)
                else:
                    for value in Parqueo.objects.all():
                        item = value.toJSON()
                        data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
       
        return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Listado de Parquos'
        context['create_url'] = reverse_lazy('erp:parqueo_create')
        context['list_url'] = reverse_lazy('erp:parqueo_list')
        context['entidad'] = 'Parqueos'
        return context
class UpdateViewParqueo(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Parqueo
    form_class = FormParqueo
    template_name = 'parqueo/create.html'
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
        context['title'] = 'Edición de un Parqueo'
        context['entidad'] = 'Parqueos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
class DeleteViewParqueo(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Parqueo
    template_name = 'parqueo/delete.html'
    success_url = reverse_lazy('erp:parqueo_list')
    
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
        context['title'] = 'Eliminación de un Parqueo'
        context['Entidad'] = 'Parqueo'
        context['list_url'] = self.success_url
        return context