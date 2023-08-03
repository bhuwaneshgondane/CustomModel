# Generated by Django 4.2.4 on 2023-08-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='India', max_length=50, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='user',
            name='dateofbirth',
            field=models.DateField(default=None, verbose_name='Birth Date '),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=64, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=64, verbose_name='State'),
        ),
    ]
