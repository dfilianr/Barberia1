# Generated by Django 4.2.16 on 2024-11-06 08:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_barbero_delete_cita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.date(2024, 11, 6), null=True)),
                ('plan', models.CharField(blank=True, choices=[('B', 'Básico $3'), ('D', 'Deluxe $4'), ('V', 'VIP $8')], default='B', max_length=1, null=True)),
                ('horarioAtencion', models.CharField(blank=True, choices=[('1', '10:00 a 11:00'), ('2', '11:00 a 12:00'), ('3', '13:00 a 14:00'), ('4', '14:00 a 15:00'), ('5', '13:00 a 16:00'), ('6', '16:00 a 17:00'), ('7', '17:00 a 18:00'), ('8', '18:00 a 19:00'), ('9', '19:00 a 20:00')], default='1', max_length=1, null=True)),
                ('barbero', models.ForeignKey(default=140725746207160, on_delete=django.db.models.deletion.CASCADE, to='core.barbero')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]