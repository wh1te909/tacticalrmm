# Generated by Django 3.1.5 on 2021-01-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_user_agent_dblclick_action"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="default_agent_tbl_tab",
            field=models.CharField(
                choices=[
                    ("server", "Servers"),
                    ("workstation", "Workstations"),
                    ("mixed", "Mixed"),
                ],
                default="server",
                max_length=50,
            ),
        ),
    ]
