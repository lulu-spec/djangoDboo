# Generated by Django 3.1.4 on 2020-12-12 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0013_aparece_ventas'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='proveedores',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proyecto.proveedor'),
            preserve_default=False,
        ),
    ]
