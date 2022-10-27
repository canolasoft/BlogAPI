# Generated by Django 3.1.7 on 2022-10-27 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='texto_e',
        ),
        migrations.AddField(
            model_name='entrada',
            name='descripcion_e',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id_t', models.BigAutoField(primary_key=True, serialize=False)),
                ('texto_t', models.CharField(max_length=1000, null=True)),
                ('imagen_t', models.ImageField(blank=True, null=True, upload_to='')),
                ('id_c', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapi.entrada')),
            ],
        ),
    ]
