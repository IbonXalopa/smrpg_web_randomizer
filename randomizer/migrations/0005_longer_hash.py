# Generated by Django 2.1.4 on 2019-01-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer', '0004_flags_json_add_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='hash',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]