# Generated by Django 2.2.1 on 2019-12-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='defenceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sId', models.CharField(max_length=1000)),
                ('sName', models.CharField(max_length=1000)),
                ('batch', models.CharField(max_length=1000)),
                ('semester', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=1000)),
                ('pNumber', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
