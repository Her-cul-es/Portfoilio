# Generated by Django 4.2.13 on 2024-05-20 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='certifications',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='father_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_experience',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Certification',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]