# Generated by Django 3.1.1 on 2020-09-25 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_responded', models.DateField(auto_now=True)),
                ('subject', models.CharField(max_length=150)),
                ('sender', models.CharField(max_length=150)),
                ('files', models.FileField(upload_to=None)),
                ('num_of_file', models.IntegerField()),
                ('date_of_file', models.DateField()),
                ('date_recived', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='sent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to=None)),
                ('subject', models.CharField(max_length=150)),
                ('sent_to', models.CharField(max_length=150)),
                ('notes', models.CharField(max_length=350)),
                ('refrence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg_app.entry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
