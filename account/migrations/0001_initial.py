# Generated by Django 4.2.15 on 2024-08-16 04:42

import account.models
import account.utils
from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "account_balance",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
                ),
                (
                    "account_number",
                    models.CharField(
                        default=account.utils.create_new_ref_number,
                        editable=False,
                        max_length=10,
                        unique=True,
                    ),
                ),
                (
                    "account_id",
                    models.CharField(
                        default=account.utils.create_new_ref_number,
                        editable=False,
                        max_length=15,
                        unique=True,
                    ),
                ),
                (
                    "pin_number",
                    models.CharField(
                        default=account.utils.create_new_ref_pin, max_length=4
                    ),
                ),
                (
                    "ref_code",
                    shortuuidfield.fields.ShortUUIDField(
                        blank=True, editable=False, max_length=22, unique=True
                    ),
                ),
                (
                    "account_status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("pending", "Pending"),
                            ("in-active", "In-active"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("kyc_submitted", models.BooleanField(default=False)),
                ("kyc_approved", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="KYC",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(
                        default="default.jpg",
                        upload_to=account.models.user_directory_path,
                    ),
                ),
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
                    "account",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.account",
                    ),
                ),
            ],
        ),
    ]
