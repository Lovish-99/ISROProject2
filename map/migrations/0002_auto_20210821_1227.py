# Generated by Django 3.2.6 on 2021-08-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='insertddl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Search',
        ),
    ]