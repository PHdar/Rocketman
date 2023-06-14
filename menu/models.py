from django.db import models
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key


from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from django_extensions.db.models import AutoSlugField
from wagtail.admin.panels import FieldPanel,PageChooserPanel,InlinePanel
from wagtail.models import Orderable


class MenuItem (Orderable):
    link_title = models.CharField(blank=True,max_length=50)
    link_url = models.CharField(max_length=500,blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page', 
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE
    )   
    open_in_new_tab = models.BooleanField(default=False,blank=True)

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    page = ParentalKey("Menu",related_name="menu_items")
    
    @property
    def link(self) -> str:
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return "#"
    
    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_title
        elif self.link_title:
            return self.link_title
        return "Missing title"
        

class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from = "title",
        editable=True,
    )
    
    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        InlinePanel("menu_items",label="Menu item")
    ]

    def __str__(self) -> str:
        return self.title
    
    def save(self, **kwargs):
        key = make_template_fragment_key(
            "site_header"
        )

        key = make_template_fragment_key(
            "site_footer"
        )
        cache.delete(key)
        
        return super().save(**kwargs)
