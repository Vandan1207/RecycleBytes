# Generated by Django 5.0.1 on 2024-02-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0005_checkout_approxweight'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='emial',
            new_name='email',
        ),
        migrations.AddField(
            model_name='checkout',
            name='timeslot',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
