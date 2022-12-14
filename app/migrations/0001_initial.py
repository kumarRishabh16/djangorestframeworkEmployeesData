# Generated by Django 4.1 on 2022-11-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employees",
            fields=[
                ("emp_no", models.IntegerField(primary_key=True, serialize=False)),
                ("birth_date", models.DateField()),
                ("first_name", models.CharField(max_length=14)),
                ("last_name", models.CharField(max_length=14)),
                ("email", models.EmailField(max_length=254)),
                (
                    "designation",
                    models.CharField(
                        choices=[
                            ("Manager", "Manager"),
                            ("Developer", "Developer"),
                            ("Tester", "Tester"),
                            ("Designer", "Designer"),
                            ("Architect", "Architect"),
                            ("Team Lead", "Team Lead"),
                            ("Project Manager", "Project Manager"),
                            ("Business Analyst", "Business Analyst"),
                            ("HR", "HR"),
                            ("Admin", "Admin"),
                            ("Other", "Other"),
                        ],
                        max_length=100,
                    ),
                ),
                ("gender", models.CharField(max_length=1)),
                (
                    "profile_image",
                    models.ImageField(blank=True, upload_to="profile_image"),
                ),
                ("documents", models.FileField(blank=True, upload_to="documents")),
            ],
        ),
    ]
