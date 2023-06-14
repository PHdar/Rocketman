from wagtail.contrib.modeladmin.options import ( modeladmin_register,ModelAdmin)
from .models import Testimodial


@modeladmin_register
class TestimonialAdmin(ModelAdmin):
    """Testimonial admin"""
    model = Testimodial
    menu_label = "Testimonials"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("quote", "attribution")
    search_fields = ("quote","attribution")