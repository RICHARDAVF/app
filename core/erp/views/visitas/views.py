
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
from datetime import date,datetime,time
# Create your views here.
class CreateViewVisita(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    user = ''
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
        form.fields['n_parqueo'].queryset=Parqueo.objects.filter(estado=True,empresa_id=self.request.user.empresa_id,
                                                        unidad_id=self.request.user.unidad_id,
                                                        puesto_id=self.request.user.puesto_id)
        form.fields['sala'].queryset=Salas.objects.filter(estado=0,empresa_id=self.request.user.empresa_id,
                                                        unidad_id=self.request.user.unidad_id,
                                                        puesto_id=self.request.user.puesto_id)
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
                    if request.user.is_superuser:
                        
                        for value in Visitas.objects.select_related("p_visita").all():
                            item = value.toJSON()
                            if  value.p_visita is not None:
                                item['p_visita'] = f"{value.p_visita.nombre} {value.p_visita.apellidos}"
                            data.append(item)
                    else:
                        for value in Visitas.objects.select_related("p_visita").filter(user_id=self.request.user.id):
                            item = value.toJSON()
                            item['p_visita'] = f"{value.p_visita.nombre} {value.p_visita.apellidos}"
                            data.append(item)
                    
                except Exception as e:
                    data = {}
                    data['error'] = str(e)
            elif action =="addperson":
                try:
                    data = {'asis':[],'parking':[]}
                    for index,value in  enumerate(Asistentes.objects.filter(visita_id=request.POST['id'])):
                        item = value.toJSON()
                        data['asis'].append(item)
                   
                    for value in Parqueo.objects.filter(estado=True,
                                                        empresa_id=request.user.empresa_id,
                                                        unidad_id=request.user.unidad_id,
                                                        puesto_id=request.user.puesto_id
                                                        ):
                        item = value.toJSON()
                        data['parking'].append(item)
                except Exception as e:
                    data['error'] = f"Ocurrio un erro {str(e)}"
            elif action =='confirm':
                Visitas.objects.filter(id=request.POST['id']).update(h_llegada=datetime.now().strftime('%H:%M:%S'),estado=2)
            elif action =='h_final':
                Visitas.objects.filter(id=request.POST['id']).update(h_termino=datetime.now().strftime('%H:%M:%S'),estado=3)
            elif action =="addvh":
                data = {}
                for value in Visitas.objects.filter(id=request.POST['id']).values_list("v_marca", "v_modelo", "v_placa", "fv_soat", "observacion","n_parqueo"):
                    try:
                        parqueo = Parqueo.objects.get(id=value[5]).numero
                    except:
                        parqueo = None
                    data['vh']={"v_marca":value[0],"v_modelo":value[1],"v_placa":value[2],"fv_soat":"-".join(str(i) for i in reversed(str(value[3]).split('/'))),"observacion":value[4],"n_parqueo":parqueo}
                parqueos = []
                for value in Parqueo.objects.filter(estado=1,puesto_id=request.user.puesto_id).values_list("id","numero"):
                    parqueos.append({"id":value[0],"numero":value[1]})
                data['parking']=parqueos
            elif action=="h_salida":
                Visitas.objects.filter(id=request.POST['id']).update(h_salida=datetime.now().strftime("%H:%M:%S"))
            elif action=="anular":
                Visitas.objects.filter(id=request.POST['id']).update(estado=0,h_llegada=time(0,0),h_salida=time(0,0))
            elif action == "formvh":
                print(request.POST)
                Visitas.objects.filter(id=request.POST['id']).update(
                    v_marca=request.POST['v_marca'],
                    v_modelo=request.POST['v_modelo'],
                    v_placa=request.POST['v_placa'],
                    fv_soat = request.POST['fv_soat'],
                    observacion = request.POST['observacion'],
                    n_parqueo = int(request.POST['n_parqueo'])
                )
                Parqueo.objects.filter(id=request.POST['n_parqueo']).update(estado=0)
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
                
                sala = request.POST['sala']
                try:
                    Salas.objects.filter(sala=sala).update(estado=1)

                except:
                    pass
                if request.POST['h_termino']!='':
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
        data = {}
        if request.POST['action'] == "addperson":
            id = request.POST['id']
            if request.POST['soat_v']=='':
                fecha =date.today()
            else:
                fecha = request.POST['soat_v']
            
            try:
                sctr = request.FILES.get('sctr', None)
                asis = Asistentes.objects.create(
                        visita_id=int(id),
                        documento=request.POST['documento'],
                        nombre=request.POST['nombre'],
                        apellidos = request.POST['apellidos'],
                        empresa = request.POST['empresa'],
                        marca_v=request.POST['marca_v'],
                        modelo_v=request.POST['modelo_v'],
                        placa_v=request.POST['placa_v'],
                        soat_v=fecha,
                        sctr=sctr,
                        n_parqueo_id=request.POST['n_parqueo'],
                    )
                asis.save()
            except Exception as e:
                print(e)
                data['error'] = f"Ocurrio un error: {str(e)}"
        return JsonResponse(data,safe=False)
    