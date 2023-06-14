# Generated by Django 4.2.1 on 2023-05-30 08:04

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('Title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', required=True))])), ('cards', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Bold title text for this card. Max length is 100 characters', max_length=100)), ('text', wagtail.blocks.TextBlock(help_text='Optional for this card', max_length=255)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automatically cropped 570px by 370px'))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
