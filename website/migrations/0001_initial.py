# Generated by Django 5.0.2 on 2024-02-28 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BatchBanner",
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
                    "batch_image",
                    models.ImageField(db_column="batch-image", upload_to="images/"),
                ),
            ],
            options={
                "db_table": "batch-banner",
            },
        ),
        migrations.CreateModel(
            name="Blogs",
            fields=[
                (
                    "blog_title",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("blog_description", models.CharField(max_length=255)),
                ("blog_content", models.TextField()),
                ("blog_author", models.CharField(max_length=255)),
                ("blog_date", models.DateField()),
                ("blog_image", models.ImageField(upload_to="images/")),
            ],
            options={
                "db_table": "blogs",
            },
        ),
        migrations.CreateModel(
            name="CourseCoverMainTopic",
            fields=[
                (
                    "topic_title",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("time", models.DateTimeField()),
            ],
            options={
                "db_table": "course-cover-main-topic",
            },
        ),
        migrations.CreateModel(
            name="Courses",
            fields=[
                (
                    "course_name",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("course_headline", models.CharField(max_length=225)),
                ("course_image", models.ImageField(upload_to="images/")),
                ("course_duration", models.CharField(max_length=255)),
                ("lecture_duration", models.CharField(max_length=255)),
                ("job_opportunity", models.CharField(max_length=255)),
                ("popular", models.BooleanField()),
                ("footer", models.BooleanField()),
            ],
            options={
                "db_table": "courses",
            },
        ),
        migrations.CreateModel(
            name="CoursesCategory",
            fields=[
                (
                    "category_name",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
            ],
            options={
                "db_table": "courses_category",
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "event_name",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("event_description", models.CharField(max_length=300)),
                ("event_start_time", models.TimeField()),
                ("event_end_time", models.TimeField()),
                ("event_venue", models.CharField(max_length=255)),
                ("event_link", models.TextField()),
                ("event_date", models.DateField()),
            ],
            options={
                "db_table": "event",
            },
        ),
        migrations.CreateModel(
            name="Review",
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
                ("name", models.CharField(max_length=100)),
                ("review", models.TextField()),
                ("position", models.CharField(blank=True, max_length=100, null=True)),
                ("link", models.TextField()),
            ],
            options={
                "db_table": "review",
            },
        ),
        migrations.CreateModel(
            name="TrendingCourses",
            fields=[
                (
                    "course_name",
                    models.OneToOneField(
                        db_column="course_name",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="website.courses",
                    ),
                ),
            ],
            options={
                "db_table": "trending_courses",
            },
        ),
        migrations.CreateModel(
            name="CourseOverview",
            fields=[
                (
                    "overview_title",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("overview_content", models.TextField()),
                (
                    "course_name",
                    models.OneToOneField(
                        db_column="course_name",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="website.courses",
                    ),
                ),
            ],
            options={
                "db_table": "course-overview",
            },
        ),
        migrations.CreateModel(
            name="CourseCoverSubTopic",
            fields=[
                (
                    "sub_topic_title",
                    models.CharField(max_length=254, primary_key=True, serialize=False),
                ),
                (
                    "main_topic_title",
                    models.ForeignKey(
                        db_column="main_topic_title",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="website.coursecovermaintopic",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        db_column="course",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="website.courses",
                    ),
                ),
            ],
            options={
                "db_table": "course-cover-sub-topic",
            },
        ),
        migrations.AddField(
            model_name="coursecovermaintopic",
            name="course",
            field=models.ForeignKey(
                db_column="course",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="website.courses",
            ),
        ),
        migrations.CreateModel(
            name="CareerOpportunities",
            fields=[
                (
                    "career_opportunity",
                    models.CharField(
                        db_column="career-opportunity",
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        db_column="course",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="website.courses",
                    ),
                ),
            ],
            options={
                "db_table": "career-opportunities",
            },
        ),
        migrations.AddField(
            model_name="courses",
            name="course_cat",
            field=models.ForeignKey(
                db_column="course_cat",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="website.coursescategory",
            ),
        ),
    ]