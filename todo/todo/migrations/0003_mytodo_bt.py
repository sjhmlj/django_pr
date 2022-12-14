# Generated by Django 4.1.1 on 2022-09-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_mytodo"),
    ]

    operations = [
        migrations.CreateModel(
            name="myTodo_bt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=80)),
                ("priority", models.IntegerField()),
                ("completed", models.BooleanField(default=False)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("deadline", models.DateField(null=True)),
                ("edit", models.IntegerField(null=True)),
            ],
        ),
    ]
