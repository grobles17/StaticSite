from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINKS = "link"
    IMAGES = "image"

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
    #return all properties and the Enum property return the value
    #value meaning the tag set along with the Enum type eg: Enum(TextType).TEXT_BOLD

