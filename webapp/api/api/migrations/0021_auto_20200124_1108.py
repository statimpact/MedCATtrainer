# Generated by Django 2.2.9 on 2020-01-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_projectannotateentities_train_model_on_submit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectannotateentities',
            name='require_entity_validation',
            field=models.BooleanField(default=True),
        ),
    ]
