# Generated by Django 3.2 on 2022-05-31 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_worker', '0023_healthworker_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthworker',
            name='age',
            field=models.CharField(max_length=4, null=True),
        ),
    ]