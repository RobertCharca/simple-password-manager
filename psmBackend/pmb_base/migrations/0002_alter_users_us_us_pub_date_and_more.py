# Generated by Django 4.1.2 on 2022-10-24 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmb_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_us',
            name='us_pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='users_us',
            name='us_upd_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
