from django.db import models
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key


from wagtail.models import Page
from wagtail.admin.panels import FieldPanel,PageChooserPanel
from wagtail.fields import StreamField
from wagtail.snippets.blocks import SnippetChooserBlock


from streams import blocks





class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["flex.FlexPage","services.ServicesListingPage","contact.ContactPage"]
    lead_text = models.CharField(
        max_length=140,
        blank=True,
        help_text='Subheading text under the banner title',
    )

    button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an optional page to link to',
        on_delete=models.SET_NULL,
    )

    button_text = models.CharField(
        max_length=50,
        default='Read more',
        blank=False,
        help_text='Button text'
    )

    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='The banner Background Image',
        on_delete=models.SET_NULL,
    )

    body = StreamField([
        ('Title',blocks.TitleBlock()),
        ('cards',blocks.CardsBlock()),
        ('image_and_text',blocks.ImageAndTextBlock()),
        ('cta',blocks.CallToActionBlock()),
        ('testimonials',SnippetChooserBlock(
            target_model='testtimonials.Testimodial',
            template = "streams/testtimonial_block.html"
        )),
        ('pricing_table',blocks.PricingTableBlock())
    ],
        null=True,
        blank=True,
        use_json_field=True)

    
    content_panels = Page.content_panels + [
        FieldPanel('lead_text'),
        PageChooserPanel('button'),
        FieldPanel('button_text'),
        FieldPanel('banner_background_image'),
        FieldPanel('body'),
    ]

    def save(self,*args,**kwargs):
        key = make_template_fragment_key (
            "home_page_streams",
            [self.id],
        )
        cache.delete(key)

        return super().save(*args,**kwargs)