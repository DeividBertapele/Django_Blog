# Generated by Django 4.2 on 2023-05-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_post_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="uplaods/"),
        ),
    ]
