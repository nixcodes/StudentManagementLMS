# Generated by Django 3.1.7 on 2021-02-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=255)),
                ('remarks', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('mark', models.CharField(default='0', max_length=255)),
            ],
        ),
    ]
