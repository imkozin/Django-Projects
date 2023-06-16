# Generated by Django 4.2.2 on 2023-06-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'My Task', 'verbose_name_plural': 'My Tasks'},
        ),
        migrations.AddField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]