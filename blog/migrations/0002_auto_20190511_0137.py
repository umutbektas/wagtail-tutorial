# Generated by Django 2.2.1 on 2019-05-10 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogdetailpage',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='bloglistingpage',
            options={'verbose_name': 'Blog Page', 'verbose_name_plural': 'Blog Page'},
        ),
    ]