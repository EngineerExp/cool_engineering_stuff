from converter import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
import re

def split_nodes_image(old_node: TextNode):
    images = extract_markdown_images(old_node.text)
    if not images:
        return [old_node]
    
    split_nodes = []
    current_text = old_node.text
    for alt_text, url in images:
        pattern = re.escape(f"![{alt_text}]({url})")
        parts = re.split(pattern, current_text, maxsplit=1)
        
        if parts[0]:
            split_nodes.append(TextNode(text_type=TextType.TEXT, text=parts[0]))
        
        split_nodes.append(TextNode(text_type=TextType.IMAGE, text=alt_text, url=url))
        
        current_text = parts[1] if len(parts) > 1 else ""
    
    if current_text:
        split_nodes.append(TextNode(text_type=TextType.TEXT, text=current_text))
    
    return split_nodes

def split_nodes_link(old_node: TextNode):
    links = extract_markdown_links(old_node.text)
    if not links:
        return [old_node]
    
    split_nodes = []
    current_text = old_node.text
    for link_text, url in links:
        pattern = re.escape(f"[{link_text}]({url})")
        parts = re.split(pattern, current_text, maxsplit=1)
        
        if parts[0]:
            split_nodes.append(TextNode(text_type=TextType.TEXT, text=parts[0]))
        
        split_nodes.append(TextNode(text_type=TextType.LINK, text=link_text, url=url))
        
        current_text = parts[1] if len(parts) > 1 else ""
    
    if current_text:
        split_nodes.append(TextNode(text_type=TextType.TEXT, text=current_text))
    
    return split_nodes

if __name__ == "__main__":
    # # Testing split_nodes_image
    # tn_image = TextNode(text_type=TextType.TEXT, text="Here is an image ![Alt text](http://example.com/image.png) and some more text.")
    # split_image_nodes = split_nodes_image(tn_image)
    # for node in split_image_nodes:
    #     print(node)

    # # Testing split_nodes_link
    # tn_link = TextNode(text_type=TextType.TEXT, text="Here is a link [Example](http://example.com) and some more text with another link [example2](http://example2.com).")
    # split_link_nodes = split_nodes_link(tn_link)
    # for node in split_link_nodes:
    #     print(node)

    # #Testing split_nodes_image and split_nodes_link together
    tn_both = TextNode(text_type=TextType.TEXT, text="Check this image ![Alt](http://example.com/img.png) and this link [Link](http://example.com).")
    split_image_then_link = []
    for node in split_nodes_image(tn_both):
        split_image_then_link.extend(split_nodes_link(node))
    for node in split_image_then_link:  
        print(node)
    
    # # testing split_nodes_link without links
    # tn_no_link = TextNode(text_type=TextType.TEXT, text="This text has no links.")
    # split_no_link = split_nodes_link(tn_no_link)
    # for node in split_no_link:
    #     print(node)
    
    # # testing split_nodes_image without images
    # tn_no_image = TextNode(text_type=TextType.TEXT, text="This text has no images.")
    # split_no_image = split_nodes_image(tn_no_image)
    # for node in split_no_image:
    #     print(node)