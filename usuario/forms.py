from django import forms

from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='input'
        self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['password'].widget.attrs['class']='input'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'


class FormularioUsuario(forms.ModelForm):
    """
    formulario de registro de un usuario en la base de datos
    
    """
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'input',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required',
        }
    ))

    password2=forms.CharField(label='Contraseña de confirmacion', widget=forms.PasswordInput(
        attrs={
            'class':'input',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
            }
    ))
    class Meta:
        model = Usuario
        fields=['email', 'username', 'nombres', 'apellidos']
        widgets={
            'email':forms.EmailInput(
                attrs={
                    'class':'input',
                    'placeholder':'Correo electrónico',
                    'id':'email',
                }
            ),
            'nombres':forms.TextInput(
                attrs={
                    'class':'input',
                    'placeholder':'Ingrese su nombre',
                    'id':'nombres',
                }
            ),
            'apellidos':forms.TextInput(
                attrs={
                    'class':'input',
                    'placeholder':'Ingrese su apellido',
                    'id':'apellidos'

                }
            ),
            'username':forms.TextInput(
                attrs={
                    'class':'input',
                    'placeholder':'Ingrese su nombre de usuario',
                    'id':'username'
                }
            )
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    
    def save(self, commit = True):
        user= super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user