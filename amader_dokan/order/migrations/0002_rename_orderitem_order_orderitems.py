# Generated by Django 4.0.3 on 2022-03-26 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderitem',
            new_name='orderitems',
        ),
    ]