from wagtail.core import blocks
from wagtail.images import blocks as image_blocks
from wagtail.snippets import blocks as snippet_blocks


class ImageBlock(blocks.StructBlock):
    image = image_blocks.ImageChooserBlock(label="Image", required=True)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Image"


class HeadlineBlock(blocks.StructBlock):
    heading = blocks.TextBlock(label="Heading", required=True, default="")
    sub_heading = blocks.TextBlock(label="Sub heading", required=False, default="")
    intro = blocks.TextBlock(label="Intro", required=False, default="")
    cta_text = blocks.TextBlock(label="CTA text", required=False, default="")
    cta_page = blocks.PageChooserBlock(label="CTA page", required=False, page_type=[])
    cta_url = blocks.URLBlock(label="CTA URL", required=False, default="")
    icon = blocks.ChoiceBlock(
        label="Icon", required=False, choices=[("leaf", "Leaf")], default=""
    )
    dark_background = blocks.BooleanBlock(
        label="Dark background", required=False, default=False
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Headline"


class TeaserBlock(blocks.StructBlock):
    blog_chooser = blocks.PageChooserBlock(
        label="Blog chooser", required=True, page_type=[]
    )
    image = image_blocks.ImageChooserBlock(label="Image", required=False)
    page_chooser = blocks.PageChooserBlock(
        label="Page chooser", required=False, page_type=[]
    )
    url_chooser = blocks.URLBlock(label="URL chooser", required=False, default="")

    class Meta:
        icon = "fa/object-group-solid"
        label = "Teaser"


class StandaloneCTABlock(blocks.StructBlock):
    text = blocks.TextBlock(label="Text", required=True, default="")
    short_description = blocks.TextBlock(
        label="Short description", required=False, max_length=100, default=""
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Standalone CTA"


class HighlightBlock(blocks.StructBlock):
    image = image_blocks.ImageChooserBlock(label="Image", required=True)
    heading = blocks.TextBlock(
        label="Heading", required=True, max_length=100, default=""
    )
    description = blocks.TextBlock(label="Description", required=False, default="")
    cta_text = blocks.TextBlock(label="CTA text", required=False, default="")
    cta_page = blocks.PageChooserBlock(label="CTA page", required=False, page_type=[])
    cta_url = blocks.URLBlock(label="CTA URL", required=False, default="")
    subheading = blocks.TextBlock(label="Subheading", required=False, default="")
    icon = blocks.ChoiceBlock(
        label="Icon", required=False, choices=[("leaf", "Leaf")], default=""
    )
    image_on_right = blocks.BooleanBlock(
        label="Image on right", required=False, default=False
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Highlight"


class IconBulletsBlock(blocks.StructBlock):
    heading = blocks.TextBlock(label="Heading", required=True, default="")
    cta_url = blocks.URLBlock(label="CTA URL", required=False, default="")
    cta_page = blocks.PageChooserBlock(label="CTA page", required=False, page_type=[])
    icon = blocks.ChoiceBlock(
        label="Icon", required=True, choices=[("leaf", "Leaf")], default=""
    )
    description = blocks.TextBlock(label="Description", required=False, default="")
    cta_text = blocks.TextBlock(label="CTA text", required=False, default="")

    class Meta:
        icon = "fa/object-group-solid"
        label = "Icon bullets"


class QuotesBlock(blocks.StructBlock):
    heading = blocks.TextBlock(label="Heading", required=True, default="")
    quote_text = blocks.TextBlock(label="Quote text", required=False, default="")
    author_name = blocks.TextBlock(label="Author name", required=True, default="")
    author_image = image_blocks.ImageChooserBlock(label="Author image", required=False)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Quotes"


class GetStartedChooserBlock(blocks.StructBlock):
    heading = blocks.TextBlock(label="Heading", required=True, default="")
    choose = snippet_blocks.SnippetChooserBlock(
        label="Choose", required=False, target_model="snippets.GetStarted"
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Get started chooser"
