# Generated by Django 5.0.3 on 2024-11-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_staff_totalleaves_alter_staff_basic_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='remainingleaves',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]