# Generated by Django 3.2.5 on 2021-08-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('picture', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d')),
                ('Nationality', models.CharField(max_length=40)),
                ('created', models.DateTimeField(auto_now=True)),
                ('Born_on', models.DateField()),
                ('Marital_Status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=15)),
                ('phone', models.CharField(blank=True, max_length=16)),
                ('email', models.EmailField(max_length=60)),
                ('address', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=30)),
                ('PERSONAL_STATEMENT', models.TextField(max_length=500)),
                ('University', models.CharField(blank=True, max_length=20, null=True)),
                ('specialty', models.CharField(blank=True, max_length=20, null=True)),
                ('grade', models.CharField(blank=True, max_length=20, null=True)),
                ('about_uni', models.TextField(blank=True, max_length=400, null=True)),
                ('course', models.CharField(max_length=30)),
                ('about_course', models.TextField(max_length=400)),
                ('ADDITIONAL_SKILLS', models.CharField(max_length=20)),
            ],
        ),
    ]
