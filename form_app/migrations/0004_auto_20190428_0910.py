# Generated by Django 2.2 on 2019-04-28 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0003_owner_model_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner_model',
            name='player1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player10',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player10', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player11',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player11', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player12',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player12', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player13',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player13', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player3',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player3', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player4',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player4', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player5',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player5', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player6',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player6', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player7',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player7', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player8',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player8', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='player9',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='player9', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='runner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='runner', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='runner2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='runner2', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='owner_model',
            name='winner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='form_app.player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.DecimalField(decimal_places=0, max_digits=20, primary_key=True, serialize=False),
        ),
    ]
