# Generated by Django 3.2.6 on 2021-08-12 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20210810_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donationhistory',
            options={'ordering': ('-date',)},
        ),
    ]
