# Generated by Django 4.2.15 on 2024-08-12 04:35

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="KYC",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                (
                    "identity_image",
                    models.ImageField(
                        default="default.jpg",
                        upload_to=account.models.user_directory_path,
                    ),
                ),
                (
                    "marital_status",
                    models.CharField(
                        choices=[
                            ("married", "Married"),
                            ("single", "Single"),
                            ("other", "Other"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "identity_type",
                    models.CharField(
                        choices=[
                            ("national_id_card", "National ID Card"),
                            ("drivers_licence", "Drives Licence"),
                            ("international_passport", "International Passport"),
                        ],
                        max_length=35,
                    ),
                ),
                ("date_of_birth", models.DateField()),
                (
                    "signature",
                    models.ImageField(
                        default="default.jpg",
                        upload_to=account.models.user_directory_path,
                    ),
                ),
                ("identity_number", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("state", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("mobile", models.CharField(max_length=15)),
                ("fax", models.CharField(max_length=15)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
