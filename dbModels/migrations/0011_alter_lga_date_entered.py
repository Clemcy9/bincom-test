# Generated by Django 4.1.7 on 2023-03-23 11:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dbModels', '0010_alter_lga_date_entered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lga',
            name='date_entered',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
