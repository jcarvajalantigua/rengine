# Generated by Django 3.0.7 on 2020-10-10 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0007_auto_20201010_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vulnerabilityscan',
            old_name='title',
            new_name='name',
        ),
    ]