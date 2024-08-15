# Generated by Django 4.2.15 on 2024-08-14 09:13

import account.utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0005_alter_account_account_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="pin_number",
            field=models.CharField(
                default=account.utils.create_new_ref_number, max_length=4
            ),
        ),
    ]
