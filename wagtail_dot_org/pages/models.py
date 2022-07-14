from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.search import index

from wagtail_dot_org import blocks as wagtail_dot_org_blocks
from wagtail_dot_org.pages import blocks as pages_blocks


class HomePage(Page):
    icon = models.CharField(
        max_length=255,
        choices=[("leaf", "Leaf"), ("arrow", "Arrow"), ("animation", "Animation")],
        verbose_name="Icon",
        blank=True,
        default="",
    )
    cta_text = models.TextField(verbose_name="CTA text", blank=True, default="")
    cta_page = models.ForeignKey(
        to="wagtailcore.Page",
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="CTA page",
        blank=True,
        null=True,
    )
    cta_url = models.URLField(verbose_name="CTA URL", blank=True, default="")
    body = StreamField(
        block_types=[
            ("headline", wagtail_dot_org_blocks.HeadlineBlock()),
            ("teaser", wagtail_dot_org_blocks.TeaserBlock()),
            ("standalonecta", wagtail_dot_org_blocks.StandaloneCTABlock()),
            ("highlight", wagtail_dot_org_blocks.HighlightBlock()),
            ("iconbullets", wagtail_dot_org_blocks.IconBulletsBlock()),
            ("quotes", wagtail_dot_org_blocks.QuotesBlock()),
            ("getstartedchooser", wagtail_dot_org_blocks.GetStartedChooserBlock()),
        ],
        default="",
        verbose_name="Body",
        blank=True,
    )
    heading = models.TextField(verbose_name="Heading", max_length=100, default="")
    sub_heading = models.TextField(verbose_name="Sub heading", blank=True, default="")
    intro = RichTextField(
        verbose_name="Intro",
        blank=True,
        features=["bold", "italic", "link"],
        default="",
    )

    hero_panels = [
        FieldPanel("heading"),
        FieldPanel("sub_heading"),
        FieldPanel("intro"),
        FieldPanel("icon"),
        FieldPanel("cta_text"),
        PageChooserPanel("cta_page"),
        FieldPanel("cta_url"),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel(heading="Hero", children=hero_panels),
        StreamFieldPanel("body"),
    ]

    search_fields = Page.search_fields + [
        index.FilterField("icon"),
        index.FilterField("cta_text"),
        index.FilterField("cta_page"),
        index.FilterField("cta_url"),
        index.SearchField("body"),
        index.FilterField("body"),
        index.SearchField("heading"),
        index.FilterField("heading"),
        index.FilterField("sub_heading"),
        index.FilterField("intro"),
    ]

    class Meta:
        verbose_name = "Homepage"


class BlogPage(Page):

    parent_page_types = [
        "pages.BlogPage",
        "pages.HomePage",
        "pages.ContentPage",
    ]

    class Meta:
        verbose_name = "Blog page"


class ContentPage(Page):
    heading = models.TextField(verbose_name="Heading", default="")
    icon = models.CharField(
        max_length=255,
        choices=[("leaf", "Leaf")],
        verbose_name="Icon",
        blank=True,
        default="",
    )
    cta_text = models.TextField(verbose_name="CTA text", blank=True, default="")
    cta_page = models.ForeignKey(
        to="wagtailcore.Page",
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="CTA page",
        blank=True,
        null=True,
    )
    cta_url = models.URLField(verbose_name="CTA URL", blank=True, default="")
    intro = RichTextField(
        verbose_name="Intro",
        blank=True,
        features=["bold", "italic", "link"],
        default="",
    )
    body = StreamField(
        block_types=[
            ("headline", wagtail_dot_org_blocks.HeadlineBlock()),
            ("teaser", wagtail_dot_org_blocks.TeaserBlock()),
            ("standalonecta", wagtail_dot_org_blocks.StandaloneCTABlock()),
            ("highlight", wagtail_dot_org_blocks.HighlightBlock()),
            ("iconbullets", wagtail_dot_org_blocks.IconBulletsBlock()),
            ("quotes", wagtail_dot_org_blocks.QuotesBlock()),
            ("getstartedchooser", wagtail_dot_org_blocks.GetStartedChooserBlock()),
            ("quote", pages_blocks.QuoteBlock()),
            ("richtext", pages_blocks.RichTextBlock()),
            ("textandmedia", pages_blocks.TextAndMediaBlock()),
            ("signupform", pages_blocks.SignupFormBlock()),
            ("comparisontable", pages_blocks.ComparisonTableBlock()),
            ("cards", pages_blocks.CardsBlock()),
        ],
        default="",
        verbose_name="Body",
        blank=True,
    )
    sub_heading = models.TextField(verbose_name="Sub heading", blank=True, default="")

    hero_panels = [
        FieldPanel("heading"),
        FieldPanel("sub_heading"),
        FieldPanel("icon"),
        FieldPanel("cta_text"),
        PageChooserPanel("cta_page"),
        FieldPanel("cta_url"),
        FieldPanel("intro"),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel(heading="Hero", children=hero_panels),
        StreamFieldPanel("body"),
    ]

    parent_page_types = [
        "pages.ContentPage",
        "pages.HomePage",
        "pages.BlogPage",
    ]

    class Meta:
        verbose_name = "Content page"
