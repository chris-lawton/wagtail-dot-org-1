from wagtail.core import blocks


class HeadingBlock(blocks.StructBlock):
    heading = blocks.TextBlock(label="Heading", required=True, default="")

    class Meta:
        icon = "fa/object-group-solid"
        label = "Heading"


class IconBlock(blocks.StructBlock):
    icon = blocks.ChoiceBlock(
        label="Icon", required=True, choices=[("leaf", "Leaf")], default=""
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Icon"


class SubheadingBlock(blocks.StructBlock):
    subheading = blocks.TextBlock(label="Subheading", required=True, default="")

    class Meta:
        icon = "fa/object-group-solid"
        label = "Subheading"


class DescriptionBlock(blocks.StructBlock):
    description = blocks.TextBlock(label="Description", required=True, default="")

    class Meta:
        icon = "fa/object-group-solid"
        label = "Description"


class PageChooserBlock(blocks.StructBlock):
    page_chooser = blocks.PageChooserBlock(
        label="Page chooser", required=True, page_type=[]
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Page chooser"


class ExternalLinkBlock(blocks.StructBlock):
    external_link = blocks.URLBlock(label="External link", required=True, default="")

    class Meta:
        icon = "fa/object-group-solid"
        label = "External link"
