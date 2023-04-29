# Generated by Django 4.1.7 on 2023-03-23 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('founding_date', models.DateTimeField(verbose_name='Founded')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('requirements', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField(verbose_name='Published')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsearch.company')),
            ],
        ),
    ]
