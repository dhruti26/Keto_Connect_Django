# Generated by Django 4.1.5 on 2023-02-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ketoconnect', '0008_alter_ketocalculator_choose_a_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='keto_age',
            name='keto_age_value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
