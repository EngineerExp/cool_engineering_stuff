from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    if part:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes

if __name__ == "__main__":
    # # # Testing split_nodes_delimiter for bold
    # tn_bold = TextNode(text_type=TextType.TEXT, text="This is **bold** text and this is **also bold**.")
    # split_bold_nodes = split_nodes_delimiter([tn_bold], "**", TextType.BOLD)
    # for node in split_bold_nodes:
    #     print(node)

    # # # Testing split_nodes_delimiter for italic
    # tn_italic = TextNode(text_type=TextType.TEXT, text="This is _italic_ text and this is _also italic_.")
    # split_italic_nodes = split_nodes_delimiter([tn_italic], "_", TextType.ITALIC)
    # for node in split_italic_nodes:
    #     print(node)

    # # # Testing split_nodes_delimiter for code
    # tn_code = TextNode(text_type=TextType.TEXT, text="This is `code` text and this is `also code`.")
    # split_code_nodes = split_nodes_delimiter([tn_code], "`", TextType.CODE)
    # for node in split_code_nodes:
    #     print(node)

    # testing combined delimiters
    tn_combined = TextNode(text_type=TextType.TEXT, text="This is **bold** text, _italic_ text, and `code` text.")
    nodes_after_bold = split_nodes_delimiter([tn_combined], "**", TextType.BOLD)
    nodes_after_italic = split_nodes_delimiter(nodes_after_bold, "_", TextType.ITALIC)
    final_nodes = split_nodes_delimiter(nodes_after_italic, "`", TextType.CODE)
    for node in final_nodes:
        print(node)