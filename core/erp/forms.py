from django.forms import ModelForm,TextInput,DateInput,TimeInput,Select,FileInput,HiddenInput
from django import forms
from .models import Visitas,Salas,Parqueo,Trabajadores,AsignacionEPPS,Vehiculos,AsignacionEV,Asistentes,IngresoSalida
from datetime import datetime

from core.user.models import Empresa,Unidad,Puesto
class FormVisitas(ModelForm):
    p_visita=forms.ModelChoiceField(queryset=Trabajadores.objects.all(),widget=forms.Select(attrs={
                "class":"form-control select2"
            }),to_field_name='id',label='Persona a quien visita')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['estado'].initial = '1'
        self.fields['tipo'].initial = '1'
        self.fields['tipo_documento'].initial = '1'
    def save(self, commit=True):
        data = {}
        form = super()
       
        try:
            if form.is_valid():
                form.save()
              
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    class Meta:
        model = Visitas
        fields = '__all__'
        widgets = {
            'user':HiddenInput(),
            'tipo_documento':Select(attrs={
                "class":'form-control',
                
            }),
            'dni':TextInput(attrs={
                'placeholder':'N° documento',
                'class':'form-control',
                'type':'number',
            }),

            'nombre':TextInput(attrs={
                'placeholder':'Nombre',
                'class':'form-control',
                
                
            }),
            'apellidos':TextInput(attrs={
                'placeholder':'Apellidos',
                'class':'form-control',
               
                
            }),
            'empresa':TextInput(attrs={
                'placeholder':'Empresa de Procedencia',
                'class':'form-control',
                
            }),
            'motivo':TextInput(attrs={
                'placeholder':'Motivo de la vista',
                'class':'form-control'
            }),
            'cargo':TextInput(attrs={
                'placeholder':'Cargo',
                'class':'form-control',
            }),
            'fecha':DateInput(format='%Y-%m-%d',
                attrs={
                'class':'form-control',
                'type':'date',
                'value':datetime.now().date
            }),
            'h_inicio':TimeInput(attrs={
                'type':'time',
                'class':'form-control',
                'value':datetime.now().strftime('%H:%M')
               
            }),
            'h_termino':TimeInput(attrs={
                'type':'time',
                'class':'form-control',
            }),
            'sala':Select(attrs={
                'class':'form-control',  
            }),
            'tipo':Select(attrs={
                'class':'form-control',  
            }),
            'v_marca' :TextInput(attrs={
                'class':'form-control',
                'placeholder':'Marca del Vehiculo'
            }),
            'v_modelo' :TextInput(attrs={
                'class':'form-control',
                'placeholder':'Modelo del Vehiculo'
            }),
            'v_placa' :TextInput(attrs={
                'class':'form-control',
                'placeholder':'Placa del Vehiculo'
            }),
            'fv_soat' :TextInput(attrs={
                'class':'form-control',
                'placeholder':'Fecha de vencimiento del SOAT'
            }),
            'sctr_salud' :FileInput(attrs={
                'class':'form-control',
            }),
            'n_parqueo':Select(attrs={
                'class':'form-control'
            }),
            'estado':Select(attrs={
                'class':'form-control'
            })
            
        }
class FormDelivery(ModelForm):
    p_visita=forms.ModelChoiceField(queryset=Trabajadores.objects.all(),widget=forms.Select(attrs={
                "class":"form-control select2"
            }),to_field_name='nombre',label='Persona a quien visita')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['estado'].initial = '2'
    def save(self,commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    class Meta:
        model = Visitas
        fields = ['estado','dni',"nombre","apellidos","guias","cantidad","tipo","observacion","empresa","user","fecha","h_inicio","h_termino","p_visita"]
        widgets= {
            'estado':Select(attrs={
                "class":"form-control",
                "type":'select'
            }),
            "dni":TextInput({
                "class":"form-control"
            }),
            "nombre":TextInput({
                "class":"form-control"
            }),
            "apellidos":TextInput({
                "class":"form-control"
            }),
            "guias":FileInput({
                "class":"form-control"
            }),
            "cantidad":TextInput({
                "class":"form-control"
            }),
            "tipo":Select({
                "class":"form-control"
            }),
            "observacion":TextInput({
                "class":"form-control"
            }),
            "empresa":TextInput({
                "class":"form-control"
            }),
            "p_visita":TextInput({
                "class":"form-control"
            }),
            "user":TextInput(attrs={
                "class":'form-control',
                'readonly':True
            }),
            'fecha':DateInput(format='%Y-%m-%d',attrs={
                'class':'form-control',
                'type':'date',
                'value':datetime.now().date
            }),
            'h_inicio':TimeInput(attrs={
                'type':'time',
                'class':'form-control',
                'value':datetime.now().strftime('%H:%M:%S')
               
            }),
            'h_termino':TimeInput(attrs={
                'type':'time',
                'class':'form-control',
                
                
            }),
        }
class FormSala(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = Salas
        fields = '__all__'
        widgets = {
            'sala':TextInput(attrs={
                'placeholder':'Numero de sala',
                'class':'form-control'
            }),
            'capacidad':TextInput(attrs={
                'placeholder':'Capacidad de la sala',
                'class':'form-control',
                'type':'number'
            }),
            'estado':HiddenInput(),
            "empresa":HiddenInput(),
            "unidad":HiddenInput(),
            "puesto":HiddenInput(),
        }
    def save(self, commit=True):
        data = {}
        form = super()
    
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
class FormParqueo(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = Parqueo
        fields = '__all__'
        widgets = {
            'numero':TextInput(attrs={
                'placeholer':'Numero de parqueo',
                'class':'form-control'
            }),
            'nombre':TextInput(attrs={
                'placeholer':'Nombre del parqueo',
                'class':'form-control'
            }),
            "estado":HiddenInput(),
            "empresa":HiddenInput(),
            "unidad":HiddenInput(),
            "puesto":HiddenInput()
        }
    def save(self, commit=True):
        data = {}
        form = super()
    
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
class FormParqueoAdmin(ModelForm):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(),widget=Select(attrs={
        'class':'form-control select2'
    }),label="Empresa")
    unidad = forms.ModelChoiceField(queryset=Unidad.objects.all(),widget=Select({
        'class':'form-control select2'
    }),label="Unidad")
    puesto = forms.ModelChoiceField(queryset=Puesto.objects.all(),widget=Select({
        'class':'form-control select2'
    }),label="Puesto")
    desde = forms.CharField(widget=TextInput(attrs={
        'class':'form-control',
        'type':'number'
    }))
    hasta = forms.CharField(widget=TextInput(attrs={
        'class':'form-control',
        'type':'number'
    }))
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = Parqueo
        exclude = ['numero','estado','unidad']
        widgets = {
            'nombre':TextInput(attrs={
                'class':'form-control',
                "placeholder":'Nombre del parqueo'
            })
        }
   
        
class FormTrabajador(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['tipo'].initial = '1'
    class Meta:
        model = Trabajadores
        fields  = "__all__"
        widgets = {
            'tipo':Select(attrs={
                'class':'form-control',
               
            }),
            'documento':TextInput(attrs={
                'class':'form-control',
                'placeholder':'0000000'
            }),
            'nombre':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Ingrese su Nombre'
            }),
            'apellidos':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Ingrese su Apellidos'
            }),
            'telefono':TextInput(attrs={
                'class':'form-control',
                'placeholder':'999999999'
            }),
            'direccion':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Ingrese su direccion'
            }),
            
            'sctr':FileInput(attrs={
                'class':'form-control',
            }),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
        
class FormEPS(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = AsignacionEPPS
        fields ='__all__'
class FormVH(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = Vehiculos
        exclude = ['trabajador']
class FormEPV(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = AsignacionEV
        fields = '__all__'
class FormAsis(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = Asistentes
        fields = "__all__"
class FormIngSal(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def save(self,commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    class Meta:
        model = IngresoSalida
        fields = "__all__"
        widgets = {
            "h_entrada":TimeInput(attrs={
                "class":'form-control form-control-sm',
                'type':'time',
                'value':datetime.now().strftime('%H:%M')
            }),
            "h_salida":TimeInput(attrs={
                "class":'form-control form-control-sm',
                'type':'time',
            }),
            "fecha":DateInput(format='%Y-%m-%d',attrs={
                "class":'form-control form-control-sm',
                'type':'date',
                'value':datetime.now().date
            }),
            "documento":DateInput(attrs={
                "class":'form-control',
                'type':'number'
            }),
            "nombres":DateInput(attrs={
                "class":'form-control',
              
            }),
            
        }
class FormEmpresa(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def save(self,commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            "ruc":TextInput(attrs={
                "class":'form-control',
                "type":"number",
            }),
            "razon_social":TextInput(attrs={
                "class":"form-control",
            }),
            "direccion":TextInput(attrs={
                "class":"form-control",
            })
        }
class FormUnidad(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    def save(self,commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    class Meta:
        model = Unidad
        fields = '__all__'
        widgets = {
            'unidad':TextInput(attrs={
                "class":'form-control'
            }),
            'empresa':Select(attrs={
                "class":'form-control'
            }),
        }
class FormPuesto(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    class Meta:
        model = Puesto
        fields = '__all__'
        widgets = {
            'unidad':Select(attrs={
                "class":'form-control'
            }),
            'puesto':TextInput(attrs={
                "class":'form-control'
            }),
            'direccion':TextInput(attrs={
                "class":'form-control'
            }),
        }
    def save(self,commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
               form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
