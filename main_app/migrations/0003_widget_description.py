# Generated by Django 2.2.3 on 2019-09-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_widget_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='description',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
