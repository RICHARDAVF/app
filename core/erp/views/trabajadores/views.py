from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,View
from core.mixins import PermisosMixins
from core.validation import Validation
from ...models import Trabajadores,AsignacionEPPS,AsignacionEV,Vehiculos
from ...forms import FormTrabajador
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from core.upload import Cargo

class CreateViewTrabajador(LoginRequiredMixin,PermisosMixins,CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'erp.add_trabajadores'
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
                data = Validation(request.POST['dni'],'dni').valid()
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
class ListViewTrabajador(LoginRequiredMixin,PermisosMixins,ListView):
    login_url = reverse_lazy('login')
    permission_required = 'erp.view_trabajadores'
    model = Trabajadores
    template_name = 'trabajadores/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def listar(self):
        data = []
       
        for value in Trabajadores.objects.all():
            item = value.toJSON()
            item['cargo'] = value.cargo.cargo
            data.append(item)
       
        return data
    def post(self, request, *args, **kwargs):
        data = {}
        # Cargo().cargar()
        # Cargo().trabajadores()
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = self.listar()
            elif action == "editepps":
                instance = AsignacionEPPS.objects.get(trabajador_id=int(request.POST["id"]))
                instance.casco = request.POST['casco']
                instance.barbiquejo = request.POST['barbiquejo']
                instance.botas = request.POST['botas']
                instance.tapones = request.POST['tapones']
                instance.lentes = request.POST['lentes']
                instance.chaleco = request.POST['chaleco']
                instance.respirador = request.POST['respirador']
                instance.save()
                data = self.listar()
            elif action == "editvh":
                instance = Vehiculos.objects.get(trabajador_id=int(request.POST['id']))
                instance.marca = request.POST['marca']
                instance.modelo = request.POST['modelo']
                instance.placa = request.POST['placa']
                instance.fv_soat = request.POST['fv_soat'],
                instance.save()
                data = self.listar()
            elif action == "editepsv":
                instance = AsignacionEV.objects.get(trabajador_id=int(request.POST['id']))
                instance.botiquin = request.POST['botiquin']
                instance.extintor = request.POST['extintor']
                instance.triangulo_s = request.POST['triangulo_s']
                instance.cono_s = request.POST['cono_s']
                instance.taco = request.POST['taco']
                instance.pertiga = request.POST['pertiga']
                instance.circulina = request.POST['circulina']
                instance.save()
                data = self.listar()
            else:
                data['error'] = 'Ha ocurrido un error'
           
        except Exception as e:
            data['error'] = str(e)
       
        return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Listado de Trabajadores'
        context['create_url'] = reverse_lazy('erp:trabajador_create')
        context['list_url'] = reverse_lazy('erp:trabajador_list')
        context['entidad'] = 'Trabajadores'
        return context
class UpdateViewTrabajador(LoginRequiredMixin,PermisosMixins,UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'erp.change_trabajadores'
    model = Trabajadores
    form_class = FormTrabajador
    template_name = 'trabajadores/create.html'
    success_url = reverse_lazy('erp:trabajador_list')
    url_redirect = success_url
    permission_denied_message = "Usted no puede accerde aqui"
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
class DeleteViewTrabajador(LoginRequiredMixin,PermisosMixins,DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'erp.delete_trabajadores'
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

class ViewEPPS(LoginRequiredMixin,PermisosMixins,View):
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
                data['pertiga'] = datos.pertiga
                data['circulina'] = datos.circulina
        except Exception as e:
            data['error'] = str(e)
       
        return JsonResponse(data, safe=False)
    