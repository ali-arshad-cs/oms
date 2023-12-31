# Generated by Django 4.2.7 on 2023-12-31 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orphan',
            name='admission_form_picture',
            field=models.ImageField(blank=True, null=True, upload_to='shared_images/'),
        ),
        migrations.AddField(
            model_name='orphan',
            name='bform_picture',
            field=models.ImageField(blank=True, null=True, upload_to='shared_images/'),
        ),
        migrations.AddField(
            model_name='orphan',
            name='orphan_picture',
            field=models.ImageField(blank=True, null=True, upload_to='shared_images/'),
        ),
        migrations.AddField(
            model_name='orphan',
            name='picture_at_time_of_admission',
            field=models.ImageField(blank=True, null=True, upload_to='shared_images/'),
        ),
        migrations.AddField(
            model_name='orphan',
            name='status',
            field=models.CharField(blank=True, choices=[('onboard', 'Onboard'), ('discharged', 'Discharged')], max_length=10),
        ),
        migrations.AlterField(
            model_name='orphan',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
    ]
