# Generated by Django 4.1.5 on 2023-02-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ketoconnect', '0007_ketocalculator_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ketocalculator',
            name='choose_a_goal',
            field=models.CharField(max_length=50),
        ),
    ]
