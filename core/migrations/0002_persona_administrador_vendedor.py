# Generated by Django 4.2.7 on 2023-11-29 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('dni', models.IntegerField(verbose_name='DNI')),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.persona')),
                ('legajo', models.IntegerField(verbose_name='Legajo')),
            ],
            bases=('core.persona',),
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.persona')),
                ('legajo', models.IntegerField(verbose_name='Legajo')),
            ],
            bases=('core.persona',),
        ),
    ]
