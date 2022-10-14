from django.db import models

from wagtail.models import Page
# from wagtail.core.fields import TextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
 
class HomePage(Page):
    description = models.TextField(
        max_length=500,
        blank=True,
        help_text = "Sous-titre sous la bannière"
    )

    button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name="+",
        help_text="Sélectionner une page à linker",
        on_delete=models.SET_NULL
    )
    button_text = models.CharField(
        max_length=50,
        default= "Read More",
        blank=False,
        help_text="Bouton pour le texte",
    )

    div_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name="+",
        help_text=" image division en bas",
        on_delete = models.SET_NULL
    )

    button_b = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name="+",
        help_text="Sélectionner une page à linker",
        on_delete=models.SET_NULL
    )

    button_b_text = models.CharField(
        max_length=50,
        default= "Read More",
        blank=False,
        help_text="Bouton pour le texte",
    )

    titre_leftdown = models.TextField(
        max_length=500,
        blank=True,
        help_text = "Sous-titre sous la bannière"
    )


    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("div_background_image"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        PageChooserPanel("button_b"),
        FieldPanel("button_b_text"),
        FieldPanel("titre_leftdown"),
    ]