# Generated by Django 3.1.4 on 2020-12-10 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0007_auto_20201210_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartado',
            name='clientes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proyecto.cliente'),
            preserve_default=False,
        ),
    ]
