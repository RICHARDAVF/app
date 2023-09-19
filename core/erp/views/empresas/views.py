from typing import Any
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from core.user.models import Empresa
from core.erp.forms import FormEmpresa
from django.http import JsonResponse
class CreateViewEmpresa(LoginRequiredMixin,CreateView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/create.html'
    success_url = reverse_lazy('erp:empresa_list')
    def post(self,request,*args,**kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = f'No se ingreso ninguna opcion'
        except Exception as e:
            data['error'] = f"Ocurrio un error: {str(e)}"
        return JsonResponse(data,safe=False)
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = "Creacion de una empresa"
        context['entidad'] = "Empresas"
        context['action'] = "add"
        context['list_url'] = self.success_url
        return context
class LisViewEmpresa(LoginRequiredMixin,ListView):
    model = Empresa
    template_name = 'empresa/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Empresas"
        context['entidad'] = "Empresas"
        context['create_url'] = reverse_lazy('erp:empresa_create')
        return context