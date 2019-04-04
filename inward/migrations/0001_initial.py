# Generated by Django 2.1.7 on 2019-04-02 21:57

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
            name='DocumentUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(upload_to='Uploads/documents')),
                ('uploaded_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_letter', models.DateField()),
                ('date_received', models.DateField()),
                ('received_from', models.CharField(max_length=200)),
                ('ref_no', models.CharField(blank=True, max_length=255)),
                ('subject', models.TextField()),
                ('officer_to', models.CharField(help_text='Officer to whom file is passed', max_length=255)),
                ('date_filed', models.DateField(help_text='Date added')),
                ('file_number', models.CharField(help_text='Complaint, purpose or issue', max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InwardPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of image file', max_length=255)),
                ('imagefile', models.ImageField(upload_to='Uploads/inward')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
