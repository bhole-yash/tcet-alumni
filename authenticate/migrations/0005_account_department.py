# Generated by Django 3.1.4 on 2021-02-07 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_auto_20210206_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='department',
            field=models.CharField(choices=[('COMP', 'Computer Engineering'), ('ELEX', 'Electronics Engineering'), ('MECH', 'Mechanical Engineering'), ('CIVIL', 'Civil Engineering'), ('EXTC', 'Electronics & Telecommunication'), ('N/A', 'Enter your Department')], default='N/A', max_length=10),
        ),
    ]