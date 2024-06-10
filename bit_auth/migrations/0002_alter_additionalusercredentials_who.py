# Generated by Django 5.0.6 on 2024-06-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bit_auth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="additionalusercredentials",
            name="who",
            field=models.CharField(
                choices=[
                    ("Admin", "Authority"),
                    ("Student", "Student"),
                    ("Faculty", "Faculty"),
                    ("Staff", "Staff"),
                ],
                max_length=30,
            ),
        ),
    ]