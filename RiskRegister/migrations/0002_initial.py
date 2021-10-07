# Generated by Django 3.2.6 on 2021-10-04 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RiskRegister', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskregister',
            name='responderID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_responderID', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='riskregister',
            name='roles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RiskRegister.severity'),
        ),
        migrations.AddField(
            model_name='riskregister',
            name='severity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RiskRegister.rsev'),
        ),
        migrations.AddField(
            model_name='riskregister',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
