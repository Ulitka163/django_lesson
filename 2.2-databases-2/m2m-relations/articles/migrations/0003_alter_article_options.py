# Generated by Django 4.0.4 on 2022-05-17 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articletag_tag_articletag_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
