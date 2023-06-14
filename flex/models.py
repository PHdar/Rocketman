from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel,PageChooserPanel
from wagtail.fields import StreamField
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail import blocks as wagtail_blocks
from wagtail.images.blocks import ImageChooserBlock

from streams import blocks

class FlexPage(Page):
    parent_page_types = ["home.HomePage","flex.FlexPage"]
    body = StreamField([
        ('Title',blocks.TitleBlock()),
        ('cards',blocks.CardsBlock()),
        ('image_and_text',blocks.ImageAndTextBlock()),
        ('cta',blocks.CallToActionBlock()),
        ('testimonials',SnippetChooserBlock(
            target_model='testtimonials.Testimodial',
            template = "streams/testtimonial_block.html"
        )),
        ('pricing_table',blocks.PricingTableBlock()),
        ('ricktext',wagtail_blocks.RichTextBlock(
            template = 'streams/simple_richtext_block.html',
            features=['bold','italic','ol','ul','link']
        )),
        ('large_image',ImageChooserBlock(
            help_text='This image will be croppedto 1200px by 775px',
            template = 'streams/large_image_block.html'
        ))
    ],
        null=True,
        blank=True,
        use_json_field=True)
    content_panels = Page.content_panels +[
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Flex (misc) page"
        verbose_name_plural = "Flex (misc) pages"
