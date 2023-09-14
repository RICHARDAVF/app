
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,View

from core.validation import Validation
from ...models import Trabajadores,AsignacionEPPS,AsignacionEV,Vehiculos
from ...forms import FormTrabajador,FormEPS,FormVH,FormEPV
from betterforms.multiform import MultiModelForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateViewTrabajador(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Trabajadores
    form_class =FormTrabajador   
    template_name = 'trabajadores/create.html'
    success_url = reverse_lazy('erp:trabajador_list')
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
            elif action =="searchdni":
                data = Validation(request.POST['dni']).valid()
            else:
                data['error'] = 'No se a ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = 'Creacion de Trabajadores'
        context['entidad'] = 'Trabajadores'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
class ListViewTrabajador(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Trabajadores
    template_name = 'trabajadores/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def listar(self):
        data = []
        for value in Trabajadores.objects.all():
            item = value.toJSON()
            data.append(item)
        return data
    def post(self, request, *args, **kwargs):
        data = {}
       
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = self.listar()
            elif action == "editepps":
               AsignacionEPPS.objects.filter(trabajador_id=int(request.POST["id"])).update(
                   casco = request.POST['casco'],
                   barbiquejo = request.POST['barbiquejo'],
                   botas = request.POST['botas'],
                   tapones = request.POST['tapones'],
                   lentes = request.POST['lentes'],
                   chaleco = request.POST['chaleco'],
                   respirador = request.POST['respirador']
               )
               data = self.listar()
            elif action == "editvh":
                Vehiculos.objects.filter(trabajador_id=int(request.POST['id'])).update(
                    marca = request.POST['marca'],
                    modelo = request.POST['modelo'],
                    placa = request.POST['placa'],
                    fv_soat = request.POST['fv_soat'],
                )
                data = self.listar()
            elif action == "editepsv":
                AsignacionEV.objects.filter(trabajador_id=int(request.POST['id'])).update(
                    botiquin = request.POST['botiquin'],
                    extintor = request.POST['extintor'],
                    triangulo_s = request.POST['triangulo_s'],
                    cono_s = request.POST['cono_s'],
                    taco = request.POST['taco'],
                )
                data = self.listar()
            else:
                data['error'] = 'Ha ocurrido un error'
           
        except Exception as e:
            data['error'] = str(e)
       
        return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Listado de Trabadores'
        context['create_url'] = reverse_lazy('erp:trabajador_create')
        context['list_url'] = reverse_lazy('erp:trabajador_list')
        context['entidad'] = 'Trabajadores'
        return context
class UpdateViewTrabajador(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Trabajadores
    form_class = FormTrabajador
    template_name = 'trabajadores/create.html'
    success_url = reverse_lazy('erp:trabajador_list')
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
        context['title'] = 'Edición de un Trabajador'
        context['entidad'] = 'Trabajadores'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
class DeleteViewTrabajador(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Trabajadores
    template_name = 'trabajadores/delete.html'
    success_url = reverse_lazy('erp:trabajador_list')
    
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
        context['title'] = 'Eliminación de un Trabajador'
        context['Entidad'] = 'Trabajadorres'
        context['list_url'] = self.success_url
        return context

class ViewEPPS(LoginRequiredMixin,View):
    login_url = reverse_lazy('login')
    model = AsignacionEPPS
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['action'] == "epps":
                datos = AsignacionEPPS.objects.get(trabajador_id=request.POST['id'])
                data['id'] = datos.id
                data['casco'] =datos.casco ==1 
                data['barbiquejo'] = datos.barbiquejo ==1 
                data['botas'] = datos.botas ==1
                data['tapones'] = datos.tapones ==1
                data['lentes'] = datos.lentes ==1
                data['chaleco'] = datos.chaleco ==1
                data['respirador'] = datos.respirador ==1
                data['action'] = "editepps"
            elif request.POST['action'] =="vh":
                datos = Vehiculos.objects.get(trabajador_id=request.POST['id'])
                data['action'] = "editvh"
                data['marca'] = datos.marca
                data['modelo'] = datos.modelo
                data['placa'] = datos.placa
                data['fv_soat'] = datos.fv_soat
            elif request.POST['action'] =="vheps":
                datos = AsignacionEV.objects.get(trabajador_id=request.POST['id'])
                data['action'] = "editepsv"
                data['botiquin'] = datos.botiquin
                data['extintor'] = datos.extintor
                data['triangulo_s'] = datos.triangulo_s
                data['cono_s'] = datos.cono_s
                data['taco'] = datos.taco
        except Exception as e:
            data['error'] = str(e)
       
        return JsonResponse(data, safe=False)
    