# Generated by Django 4.2.7 on 2024-04-23 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hydroponic_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.FloatField()),
                ('water_temperature', models.FloatField()),
                ('tds', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('hydroponic_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hydroponic_system.hydroponicsystem')),
            ],
        ),
    ]
