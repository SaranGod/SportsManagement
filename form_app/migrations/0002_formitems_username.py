# Generated by Django 2.2 on 2019-04-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formitems',
            name='username',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
