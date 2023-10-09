# Generated by Django 4.2.6 on 2023-10-07 14:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MentorRequest",
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
                ("is_accepted", models.BooleanField(default=False)),
                (
                    "mentor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Season",
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
                (
                    "name",
                    models.CharField(
                        default=projects.models.default_season_name, max_length=100
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=255)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("WEB3", "Blockchain"),
                            ("AIML", "AI/ML"),
                            ("DEV", "Development"),
                            ("CP", "Competitive Programming"),
                            ("MISC", "Miscellaneous"),
                        ],
                        max_length=4,
                    ),
                ),
                (
                    "mentee_min",
                    models.IntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(20),
                        ],
                    ),
                ),
                (
                    "mentee_max",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(20),
                        ]
                    ),
                ),
                ("abstract", models.TextField(max_length=500)),
                ("description", models.TextField()),
                (
                    "mentors",
                    models.ManyToManyField(
                        through="projects.MentorRequest", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        default=projects.models.get_current_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="projects",
                        to="projects.season",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="mentorrequest",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="projects.project"
            ),
        ),
    ]
