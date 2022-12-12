# Generated by Django 4.1.3 on 2022-12-12 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projectMainModel',
            fields=[
                ('Title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=10)),
                ('price', models.IntegerField(primary_key=True, serialize=False)),
                ('uniquecode', models.CharField(max_length=20, unique=True)),
                ('size', models.CharField(max_length=10)),
                ('quality', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='productimagemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.projectmainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='productcolourmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.projectmainmodel')),
            ],
        ),
    ]
