# Generated by Django 4.2.4 on 2023-08-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Assessment",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("course_code", models.CharField(max_length=50)),
                ("excellent_rating", models.IntegerField()),
                ("very_good_rating", models.IntegerField()),
                ("good_rating", models.IntegerField()),
                ("fair_rating", models.IntegerField()),
                ("poor_rating", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Coverage",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("course_code", models.CharField(max_length=50)),
                ("excellent_rating", models.IntegerField()),
                ("very_good_rating", models.IntegerField()),
                ("good_rating", models.IntegerField()),
                ("fair_rating", models.IntegerField()),
                ("poor_rating", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Evaluation",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("course_code", models.CharField(max_length=50)),
                ("excellent_rating", models.IntegerField()),
                ("very_good_rating", models.IntegerField()),
                ("good_rating", models.IntegerField()),
                ("fair_rating", models.IntegerField()),
                ("poor_rating", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Impact",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("course_code", models.CharField(max_length=50)),
                ("excellent_rating", models.IntegerField()),
                ("very_good_rating", models.IntegerField()),
                ("good_rating", models.IntegerField()),
                ("fair_rating", models.IntegerField()),
                ("poor_rating", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Participation",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("course_code", models.CharField(max_length=50)),
                ("excellent_rating", models.IntegerField()),
                ("very_good_rating", models.IntegerField()),
                ("good_rating", models.IntegerField()),
                ("fair_rating", models.IntegerField()),
                ("poor_rating", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="QuatitativeFeedback",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("course_code", models.CharField(max_length=50)),
                ("course_name", models.CharField(max_length=50)),
                ("student_number", models.CharField(max_length=50)),
                ("registration_number", models.CharField(max_length=50)),
                ("likes_field", models.CharField(max_length=5000)),
                ("likes_sentiment", models.IntegerField(default=0)),
                ("suggestion_field", models.CharField(max_length=5000)),
                ("suggestion_sentiment", models.IntegerField(default=0)),
            ],
        ),
    ]