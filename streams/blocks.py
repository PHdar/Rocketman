from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django import forms
from wagtail.contrib.table_block.blocks import TableBlock
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList



class TitleBlock (blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text="Text to display",
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on page"

        
class LinkValue(blocks.StructValue):
    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        else:
            return ""


class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50,
        default='More detail'
        )
    internal_page = blocks.PageChooserBlock(
        required=False
        )
    external_link = blocks.URLBlock(
        required=False
        )
    class Meta :
        value_class = LinkValue

    def clean(self, value):
        internal_page = value.get("internal_page")
        external_link =value.get("external_link")
        errors = {}
        if internal_page and external_link:
            errors['internal_page'] = ErrorList(["Both of the field can't be filled. Please select one option"])
            errors['external_link'] = ErrorList(["Both of the field can't be filled. Please select one option"])
        elif not internal_page and  not external_link:
            errors['internal_page'] = ErrorList(["Please select page or enter a link"])
            errors['external_link'] = ErrorList(["Please select page or enter a link"])
        if errors:
            raise ValidationError("Validation error in your Link",params=errors)


class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        help_text="Bold title text for this card. Max length is 100 characters"
        )
    text = blocks.TextBlock(
        max_length=255,
        help_text="Optional for this card"
        )
    image = ImageChooserBlock(
        help_text="Image will be automatically cropped 570px by 370px"
        )
    link = Link(help_text = "Enter a link or a page")

class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.field.widget = forms.RadioSelect(
            choices= self.field.widget.choices
        )



class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        Card()
    )
    class Meta:
        template="streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"

class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(help_text="Choose a Image")
    image_alignment = RadioSelectBlock(
        choices=(
            ("left","Image to the left"),
            ("right","Image to the right"),
        ),
        default="left",
        help_text="Image on the left with text"

    )
    title = blocks.CharBlock(max_length=60, help_text="Max length is 60 character")
    text = blocks.CharBlock(max_length=140,required=False)
    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"

class CallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=200,
        help_text="Max length is 200 character"
    )
    link = Link()

    class Meta:
        template = "streams/call_to_acction_block.html"
        icon = "plus"
        label = "Call to Action"

class PricingTableBlock(TableBlock):
    class Meta:
        template = 'streams/pricing_table_block.html'
        label = "Table"
        icon = "table"
        help_text = "Your pricing table should always have 4 columns"