from django.forms import ModelForm
from django import forms
from .models import User
from .models import Empresa,Unidad,Puesto
from django.contrib.auth.models import Permission


class PermissionSelectionForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(),to_field_name='username',widget=forms.Select(attrs={
        'class':'form-control',
    }),label="ID Usuario")
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    
    class Meta:
        model = User
        fields = ['user', 'permissions']
    def __init__(self, *args, **kwargs):
        super(PermissionSelectionForm, self).__init__(*args, **kwargs)
        
        if self.instance:
            # Si ya hay una instancia de usuario (edición), establece los permisos actuales en el formulario
            self.fields['user'].initial = self.instance.username
            # print(self.instance.username)
            self.fields['permissions'].initial = self.instance.user_permissions.all()
    def label_from_instance(self, obj):
        # Personaliza cómo se muestra cada opción en el elemento select
        return obj.username
class FormUser(ModelForm):
    empresa=forms.ModelChoiceField(queryset=Empresa.objects.all(),widget=forms.Select(attrs={
                "class":"form-control select2"
            }))
    unidad=forms.ModelChoiceField(queryset=Unidad.objects.all(),widget=forms.Select(attrs={
                "class":"form-control select2"
            }))
    puesto=forms.ModelChoiceField(queryset=Puesto.objects.all(),widget=forms.Select(attrs={
                "class":"form-control select2"
            }))
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password','image','groups','dni',"empresa","unidad","puesto"]
        widgets = {
            'dni':forms.TextInput(
                attrs={
                    'placeholder':'Documento',
                    'class':'form-control',
                    'type':'number'
                }
            ),
            'first_name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese sus nombres',
                    'class':'form-control',
                    'required':'true'
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese sus apellidos',
                    'class':'form-control',
                    'required':'true'
                }
            ),
            'email' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese sus correo',
                    'type':'email',
                    'class':'form-control',
                }
            ),
            'username' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese su nombre de usuario',
                    'class':'form-control',
                }
            ),
            'password':forms.PasswordInput(render_value=True,attrs={
                'placeholder':'Ingrese su contraseña',
                'class':'form-control',
            }),
            'groups': forms.SelectMultiple(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
                'multiple': 'multiple',
                 
            }),
            'image':forms.FileInput(
                attrs={
                    'class':'form-control',
                    'type':'file'
            }),
        }
        exclude = ['user_permissions','last_login','date_joined','is_superuser','is_active','is_staff']
    def save(self,commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password!=pwd:
                        u.set_password(pwd)
                u.save()
                u.groups.clear()
                for g in self.cleaned_data['groups']:
                    u.groups.add(g)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['e'] = str(e)
        return data