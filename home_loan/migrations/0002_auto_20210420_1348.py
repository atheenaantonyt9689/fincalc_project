# Generated by Django 3.1.5 on 2021-04-20 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_loan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homeloan',
            old_name='tenure',
            new_name='month',
        ),
        migrations.RenameField(
            model_name='homeloan',
            old_name='interest_rate',
            new_name='rate',
        ),
    ]
