from django import forms
from django.forms import ValidationError
from cac.models import Estudiante, Docente, Curso, Comision


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                              code='Error1',
                              params={'valor': value})
        #raise ValidationError('El nombre no puede contener números.')


class ContactoForm(forms.Form):

    TIPO_CONSULTA = (
        ('', '-Seleccione-'),
        (1, 'Inscripciones'),
        (2, 'Soporte Aula Virtual'),
        (3, 'Ser docente'),
    )

    nombre = forms.CharField(
        label='Nombre',
        required=False,
        validators=(solo_caracteres,),
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese solo texto'})
    )
    email = forms.EmailField(
        label='Email',
        max_length=50,
        error_messages={
            'required': 'Por favor completa el campo',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'type': 'email'})
    )
    asunto = forms.CharField(
        label='Asunto',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mensaje = forms.CharField(
        label='Mensaje',
        max_length=500,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    suscripcion = forms.BooleanField(
        label='Deseo suscribirme a las novedades de codo a codo',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input', 'value': 1})
    )

    tipo_consulta = forms.ChoiceField(
        label='Tipo de consulta',
        choices=TIPO_CONSULTA,
        initial='2',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError(
                "Debes especificar mejor el mensaje que nos envias")
        return data

    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get("asunto")
        suscripcion = cleaned_data.get("suscripcion")

        if suscripcion and asunto and "suscripcion" not in asunto:
            msg = "Debe agregar la palabara 'suscripcion' al asunto."
            self.add_error('asunto', msg)


# Formularios asociados a modelos
class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante
        fields = ("nombre", "apellido", "legajo",)


class DocenteForm(forms.ModelForm):

    class Meta:
        model = Docente
        fields = ("nombre", "apellido", "cuit",)


class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ("nombre",)


class ComisionForm(forms.ModelForm):

    class Meta:
        model = Comision
        fields = ['nombre', 'fecha_inicio',
                  'portada', 'descripcion', 'curso']

    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fecha_inicio = forms.DateField(
        label='Fecha Inicio',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
    )
    """Se utiliza ModelChoiceField para poder realizar un filtrado de lo que
    quiero mostrar en el selector"""
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.filter(baja=False),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    portada = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
