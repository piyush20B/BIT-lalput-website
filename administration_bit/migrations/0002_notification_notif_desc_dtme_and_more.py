# Generated by Django 5.0.6 on 2024-05-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration_bit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notif_desc_dtme',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notif_desc',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notif_title',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notify_link',
            field=models.TextField(default=None, null=True),
        ),
    ]
