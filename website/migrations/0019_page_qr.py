# Generated by Django 4.1.2 on 2022-12-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_font_page_font_alter_page_colorscheme_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='qr',
            field=models.ImageField(default='qr/default.png', upload_to='qr'),
        ),
    ]