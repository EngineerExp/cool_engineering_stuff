from htmlnode import LeafNode, ParentNode
from textnode import TextNode
import re

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case text_node.text_type.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case text_node.text_type.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case text_node.text_type.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case text_node.text_type.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case text_node.text_type.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case text_node.text_type.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.alt_text})
        case _:
            raise Exception("Unknown TextNode type")
        
def extract_markdown_images(text):
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, text)

def markdown_to_blocks(markdown_text: str) -> list[str]:
    lines = markdown_text.split("\n")
    blocks: list[str] = []
    current: list[str] = []
    in_code = False

    for line in lines:
        if line.strip().startswith("```"):
            if not in_code:
                # starting a code block
                if current:
                    blocks.append("\n".join(current).strip())
                    current = []
                in_code = True
                current.append(line)
            else:
                # ending a code block
                current.append(line)
                blocks.append("\n".join(current).strip())
                current = []
                in_code = False
            continue

        if in_code:
            current.append(line)
            continue

        # non-code handling
        if line.strip() == "":
            if current:
                blocks.append("\n".join(current).strip())
                current = []
        else:
            current.append(line)
        
        if line.strip().startswith(("#")):
            if current:
                blocks.append("\n".join(current).strip())
                current = []

    if current:
        blocks.append("\n".join(current).strip())
        
    return blocks

if __name__ == "__main__":
    #comment out if testing
    pass

    # testing the functions ....................
    
    # # Example usage
    # tn = TextNode(text_type=TextType.TEXT, text="Hello World")
    # html_node = text_node_to_html_node(tn)
    # print(html_node)

    # ## example of extract_markdown_images
    # markdown_text = "Here is an image ![Alt text](http://example.com/image.png) and some more text."
    # images = extract_markdown_images(markdown_text)
    # print(images)   

    # # example of extract_markdown_links
    # markdown_text = "Here is a link [Example](http://example.com) and some more text with another link [example2](http://example2.com)."
    # links = extract_markdown_links(markdown_text)
    # print(links)

#     # example of markdown_to_blocks
#     md = """
#              # This is a heading



# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

#            - This is the first list item in a list block                
# - This is a list item
# - This is another list item
# """
#     blocks = markdown_to_blocks(md)
#     print(blocks)