# Generated by Django 3.2.7 on 2021-09-24 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_landing_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadossite',
            name='titulo',
        ),
        migrations.AddField(
            model_name='produto',
            name='empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_landing_page.dadossite'),
        ),
    ]
