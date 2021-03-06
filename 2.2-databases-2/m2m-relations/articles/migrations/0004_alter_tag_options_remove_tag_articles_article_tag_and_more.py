# Generated by Django 4.0.4 on 2022-05-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(through='articles.ArticleTag', to='articles.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Раздел'),
        ),
    ]
