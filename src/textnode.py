from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, 
                 text: str, 
                 text_type: TextType, 
                 url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.alt_text = text if text_type == TextType.IMAGE else None
    
    def __eq__(self, other):
        if ((self.text_type == other.text_type) and
            (self.text == other.text) and
            (self.url == other.url)):
            return True
        return False
    
    def __repr__(self):
        return f'TextNode("{self.text}", {self.text_type}{f",{self.url}" if self.url else ""})'