# Generated by Django 3.1.2 on 2020-10-26 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=50)),
                ('year_release', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
