from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from wagtail_dot_org.snippets import blocks as snippets_blocks


@register_snippet
class GetStarted(models.Model):
    body = StreamField(
        block_types=[
            ("heading", snippets_blocks.HeadingBlock()),
            ("icon", snippets_blocks.IconBlock()),
            ("subheading", snippets_blocks.SubheadingBlock()),
            ("description", snippets_blocks.DescriptionBlock()),
            ("pagechooser", snippets_blocks.PageChooserBlock()),
            ("externallink", snippets_blocks.ExternalLinkBlock()),
        ],
        default="",
        verbose_name="Body",
        blank=True,
    )

    panels = [
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Get started"


@register_snippet
class SignupForm(models.Model):
    heading = models.TextField(verbose_name="Heading", default="")
    sub_heading = models.TextField(verbose_name="Sub heading", blank=True, default="")
    mailchimp_id = models.TextField(verbose_name="Mailchimp ID", blank=True, default="")

    panels = [
        FieldPanel("heading"),
        FieldPanel("sub_heading"),
        FieldPanel("mailchimp_id"),
    ]

    def __str__(self):
        if self.heading:
            return self.heading
        return super().__str__()

    class Meta:
        verbose_name = "Signup form"
