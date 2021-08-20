# Generated by Django 3.2.6 on 2021-08-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0005_campaign_withdraw_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('VERIFIED', 'VERIFIED'), ('REJECTED', 'REJECTED'), ('STOPPED', 'STOPPED')], default='PENDING', max_length=255),
        ),
    ]