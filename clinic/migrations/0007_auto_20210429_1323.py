# Generated by Django 3.2 on 2021-04-29 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_auto_20210429_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceptionPacient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_reception', models.CharField(max_length=200)),
                ('url', models.SlugField(max_length=200)),
                ('date_reception', models.DateField()),
                ('time_reception', models.TimeField()),
                ('code_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_services', to='clinic.servicelist')),
                ('number_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_cards', to='clinic.pacient')),
                ('tab_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tab_numbers', to='clinic.doctor')),
            ],
        ),
        migrations.DeleteModel(
            name='Reception',
        ),
    ]