# Generated by Django 3.1.4 on 2020-12-10 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartado',
            name='advance',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Abono'),
        ),
    ]