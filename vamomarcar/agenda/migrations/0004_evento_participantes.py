# Generated by Django 4.0.2 on 2022-02-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_alter_evento_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='participantes',
            field=models.IntegerField(default=0),
        ),
    ]
