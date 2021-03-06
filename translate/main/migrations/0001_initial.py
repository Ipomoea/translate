# Generated by Django 3.1.3 on 2020-11-22 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=64)),
                ('date_added', models.DateField(auto_now=True)),
                ('lang_key', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=64)),
                ('lang_code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Translate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=64)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.entry')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.subject')),
            ],
        ),
    ]
