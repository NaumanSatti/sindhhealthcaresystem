# Generated by Django 3.2 on 2022-05-30 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_worker', '0021_auto_20220531_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthworker',
            name='dateofbirth',
            field=models.DateTimeField(null=True),
        ),
    ]
