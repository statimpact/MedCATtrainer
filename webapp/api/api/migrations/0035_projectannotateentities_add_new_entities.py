# Generated by Django 2.2.11 on 2020-03-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20200212_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectannotateentities',
            name='add_new_entities',
            field=models.BooleanField(default=False),
        ),
    ]
