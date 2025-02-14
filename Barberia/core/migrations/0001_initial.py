# Generated by Django 4.2.16 on 2024-10-29 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barberia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='barberia_images/')),
                ('titulo', models.CharField(max_length=100)),
                ('maps', models.CharField(default='https://maps.app.goo.gl/4Z6tBPcvjYrki5nK8', max_length=100)),
                ('insta', models.CharField(default='https://www.instagram.com/', max_length=100)),
                ('descripcion', models.TextField()),
                ('ubicacion', models.CharField(choices=[('guayaquil', 'guayaquil'), ('santa-elena', 'santa-elena'), ('milagro', 'milagro'), ('duran', 'duran')], default='*', max_length=200)),
                ('numero_contacto', models.CharField(max_length=15)),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('plan', models.CharField(choices=[('Básico', 'Básico'), ('Deluxe', 'Deluxe'), ('VIP', 'VIP')], default='Básico', max_length=10)),
                ('barberia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.barberia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
