# Generated by Django 4.1.1 on 2023-01-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='test',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
