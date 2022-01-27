# Generated by Django 3.2 on 2022-01-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('date', 'play'), 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AddField(
            model_name='event',
            name='sort',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]