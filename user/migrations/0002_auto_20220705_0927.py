# Generated by Django 2.2.5 on 2022-07-05 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='员工编号'),
        ),
    ]
