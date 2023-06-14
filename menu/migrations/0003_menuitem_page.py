# Generated by Django 4.2.1 on 2023-06-10 08:35

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='page',
            field=modelcluster.fields.ParentalKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menu.menu'),
            preserve_default=False,
        ),
    ]