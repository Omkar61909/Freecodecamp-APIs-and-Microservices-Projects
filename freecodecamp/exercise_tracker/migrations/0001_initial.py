# Generated by Django 3.0.5 on 2020-05-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, editable=False, max_length=16, unique=True)),
                ('user_name', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]