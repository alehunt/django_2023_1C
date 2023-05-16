# Generated by Django 3.2 on 2023-05-16 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('baja', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, null=True)),
                ('dni', models.IntegerField(verbose_name='DNI')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.persona')),
                ('matricula', models.CharField(max_length=10, verbose_name='Matricula')),
                ('baja', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Estudiantes',
            },
            bases=('administracion.persona',),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.persona')),
                ('legajo', models.CharField(max_length=10, verbose_name='Legajo')),
            ],
            bases=('administracion.persona',),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('domicilio', models.CharField(max_length=20, verbose_name='Domicilio')),
                ('foto', models.ImageField(null=True, upload_to='perfiles/', verbose_name='Foto Perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administracion.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('fecha_inicio', models.DateField(default=None, null=True, verbose_name='Fecha de inicio')),
                ('portada', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Portada')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('horario', models.CharField(default=None, max_length=100, null=True, verbose_name='Horario')),
                ('link_meet', models.URLField(max_length=100, verbose_name='Link de Meet')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('estado', models.CharField(choices=[('INS', 'Inscripto'), ('CUR', 'Cursando'), ('EGR', 'Egresado')], default='INS', max_length=3)),
                ('comision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.comision')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.estudiante')),
            ],
        ),
        migrations.AddField(
            model_name='comision',
            name='estudiantes',
            field=models.ManyToManyField(through='administracion.Inscripcion', to='administracion.Estudiante'),
        ),
    ]