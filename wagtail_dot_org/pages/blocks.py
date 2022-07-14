from wagtail.core import blocks
from wagtail.embeds import blocks as embed_blocks
from wagtail.images import blocks as image_blocks
from wagtail.snippets import blocks as snippet_blocks


class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock(label="Quote", required=True, default="")
    author = blocks.TextBlock(label="Author", required=False, default="")
    author_image = image_blocks.ImageChooserBlock(label="Author image", required=False)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Quote"


class RichTextBlock(blocks.StructBlock):
    rich_text = blocks.RichTextBlock(
        label="Rich text",
        required=True,
        features=["bold", "italic", "h2", "h3", "ol", "ul", "link", "document"],
        default="",
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Rich text"


class TextAndMediaBlock(blocks.StructBlock):
    image = image_blocks.ImageChooserBlock(label="Image", required=False)
    embed = embed_blocks.EmbedBlock(label="Embed", required=False, default="")
    heading = blocks.TextBlock(label="Heading", required=True, default="")
    description = blocks.TextBlock(label="Description", required=True, default="")
    cta_text = blocks.TextBlock(label="CTA text", required=False, default="")
    cta_page = blocks.PageChooserBlock(label="CTA page", required=False, page_type=[])
    cta_url = blocks.URLBlock(label="CTA URL", required=False, default="")
    image_on_right = blocks.BooleanBlock(
        label="Image on right", required=False, default=False
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Text and Media"


class SignupFormBlock(blocks.StructBlock):
    signup_form = snippet_blocks.SnippetChooserBlock(
        label="Signup form", required=True, target_model="snippets.SignupForm"
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Signup form"


class ComparisonTableBlock(blocks.StructBlock):
    class Meta:
        icon = "fa/object-group-solid"
        label = "Comparison table"


class CardsBlock(blocks.StructBlock):
    cta_url = blocks.URLBlock(label="CTA URL", required=False, default="")
    cta_page = blocks.PageChooserBlock(label="CTA page", required=False, page_type=[])
    heading = blocks.TextBlock(label="Heading", required=True, default="")
    subheading = blocks.TextBlock(label="Subheading", required=True, default="")
    icon = blocks.ChoiceBlock(
        label="Icon", required=True, choices=[("leaf", "Leaf")], default=""
    )
    description = blocks.RichTextBlock(
        label="Description", required=False, features=["bold", "italic"], default=""
    )
    cta_text = blocks.PageChooserBlock(label="CTA text", required=False, page_type=[])
    image = image_blocks.ImageChooserBlock(label="Image", required=False)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Cards"
