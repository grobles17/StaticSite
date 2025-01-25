from enum import Enum

from leafnode import LeafNode

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode(): 
    def __init__(self, text: str, text_type: Enum, url = None):
        self.text = text
        self.text_type = text_type 
        self.url = url

    def __eq__(self, TextNode2):
        if (
            self.text == TextNode2.text 
            and self.text_type == TextNode2.text_type
            and self.url == TextNode2.url
        ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    #return all properties and for the Enum property return its value
    #value meaning the tag set along with the Enum type eg: Enum(TextType).TEXT_BOLD

def text_node_to_html_node(text_node: TextNode):
    """Converts a text node into a LeafNode, which has as parent HTMLNode."""
    if not isinstance(text_node.text_type, TextType):
        raise Exception("Instance has not a valid TextType")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text, tag=None)
        case TextType.BOLD:
            return LeafNode(value=text_node.text, tag="b")
        case TextType.ITALIC:
            return LeafNode(value=text_node.text, tag="i")
        case TextType.CODE:
            return LeafNode(value=text_node.text, tag="code")
        case TextType.LINK:
            return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(value="", tag="img", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Unexpected Enum value")
    