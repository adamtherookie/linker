# Generated by Django 4.1.2 on 2022-12-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_page_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='watermark',
            field=models.BooleanField(default=True),
        ),
    ]