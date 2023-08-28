from typing import Any, Dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from ...models import Salas
from ...forms import FormSala
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class CreateViewSala(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Salas
    form_class = FormSala
    template_name = 'salas/create.html'
    success_url = reverse_lazy('erp:sala_list')
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
        context['title'] = 'Creacion de una Sala'
        context['entidad'] = 'Salas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
class ListViewSala(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Salas
    template_name = 'salas/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
       
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for value in Salas.objects.all():
                    item = value.toJSON()
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
       
        return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Listado de Salas'
        context['create_url'] = reverse_lazy('erp:sala_create')
        context['list_url'] = reverse_lazy('erp:sala_list')
        context['entidad'] = 'Salas'
        return context
class UpdateViewSala(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Salas
    form_class = FormSala
    template_name = 'salas/create.html'
    success_url = reverse_lazy('erp:sala_list')
   
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
        context['title'] = 'Edición de un Sala'
        context['entidad'] = 'Salas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
class DeleteViewSala(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Salas
    template_name = 'salas/delete.html'
    success_url = reverse_lazy('erp:sala_list')
    
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
        context['title'] = 'Eliminación de un Sala'
        context['Entidad'] = 'Salas'
        context['list_url'] = self.success_url
        return context