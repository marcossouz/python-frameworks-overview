# Generated by Django 3.2.5 on 2021-07-02 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('status', models.CharField(choices=[('1', 'Open'), ('2', 'To Do'), ('3', 'Doing')], max_length=255, verbose_name='Status')),
            ],
        ),
    ]
