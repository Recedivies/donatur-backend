# Generated by Django 3.2.6 on 2021-08-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_fundraiserproposal_fundraiser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundraiserproposal',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]