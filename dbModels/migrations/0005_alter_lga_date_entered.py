# Generated by Django 4.1.7 on 2023-03-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbModels', '0004_alter_lga_date_entered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lga',
            name='date_entered',
            field=models.DateTimeField(auto_now=True),
        ),
    ]