# Generated by Django 3.1.6 on 2021-03-22 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeArticles', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]
