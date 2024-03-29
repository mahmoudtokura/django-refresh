# Generated by Django 5.0.1 on 2024-01-29 13:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0003_alter_blog_category"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blogs",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
