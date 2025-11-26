from textnode import TextNode, TextType
from split_nodes_image_and_link  import split_nodes_image, split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    initial_node = TextNode(text_type=TextType.TEXT, text=text)
    nodes = split_nodes_image(initial_node)
    nodes = [node for old_node in nodes for node in split_nodes_link(old_node)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "*", TextType.CODE)
    return nodes

if __name__ == "__main__":
    # test text_to_textnodes
    markdown_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text_nodes = text_to_textnodes(markdown_text)
    for tn in text_nodes:
        print(tn)