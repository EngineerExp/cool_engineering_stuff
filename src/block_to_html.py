from blocktype import BlockType, block_to_block_type
from htmlnode import LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from converter import markdown_to_blocks, text_node_to_html_node
from textnode import TextNode,TextType
import re

def text_to_children(text: str) -> list[LeafNode | ParentNode]:
    text_nodes = text_to_textnodes(text)
    html_children = [text_node_to_html_node(tn) for tn in text_nodes]
    return html_children

# convert markdown_to_html_node
def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    html_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                first_line = block.split("\n", 1)[0]
                first_space = first_line.find(" ")
                hashes = first_line[:first_space]
                level = hashes.count("#")
                content = first_line[first_space + 1 :].strip()
                html_children.append(
                ParentNode(
                    tag=f"h{level}",
                    children=text_to_children(content),
                )
            )
              
            case BlockType.PARAGRAPH:
                content = block.replace("\n", " ")  # Replace newlines with spaces for paragraphs
                html_children.append(
                    ParentNode(
                        tag="p",
                        children=text_to_children(content),
                    )
                )

            case BlockType.CODE:
                code_content = "\n".join(block.split("\n")[1:-1]) + "\n" # Extract code between ```
                code_node = TextNode(code_content, TextType.TEXT)
                html_children.append(
                    ParentNode(
                        tag="pre",
                        children=[
                            ParentNode(
                                tag="code",
                                children=[text_node_to_html_node(code_node)]
                            )
                        ],
                    )
                )
            # put all quoted lines into a single blockquote without separate paragraphs
            case BlockType.QUOTE:
                lines = block.split("\n") #split into lines

                # strip leading '> ' or '>' from each line
                stripped = []
                for line in lines:
                    if line.startswith(">"):
                        content = line[1:]
                        if content.startswith(" "):
                            content = content[1:]
                        stripped.append(content)
                    else:
                        stripped.append(line)
                
                quote_content = " ".join(stripped).strip()
                
                html_children.append(
                    ParentNode(
                        tag="blockquote",
                        children=text_to_children(quote_content),
                    )
                )
              
                    
            case BlockType.UNORDERED_LIST:
                list_items = []
                for line in block.split("\n"):
                    item_content = line[2:].strip()  # Remove '- ' prefix
                    list_items.append(
                        ParentNode(
                            tag="li",
                            children=text_to_children(item_content),
                        )
                    )
                html_children.append(
                    ParentNode(
                        tag="ul",
                        children=list_items,
                    )
                )
            case BlockType.ORDERED_LIST:
                list_items = []
                for line in block.split("\n"):
                    item_content = re.sub(r"^\d+\. ", "", line).strip()  # Remove 'n. ' prefix
                    list_items.append(
                        ParentNode(
                            tag="li",
                            children=text_to_children(item_content),
                        )
                    )
                html_children.append(
                    ParentNode(
                        tag="ol",
                        children=list_items,
                    )
                )
            case _:
                raise ValueError(f"Unsupported block type: {block_type}")
    return ParentNode(tag="div", children=html_children)

if __name__ == "__main__":

    # test qouoted text
    md = """# HEADING1
> This is a quoted text.
> It has multiple lines.
> And some **bold** text.
> Another paragraph in the quote.
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)

# old quote block
            # case BlockType.QUOTE:
            #     lines = block.split("\n") #split into lines

            #     # strip leading '> ' or '>' from each line
            #     stripped = []
            #     for line in lines:
            #         if line.startswith(">"):
            #             content = line[1:]
            #             if content.startswith(" "):
            #                 content = content[1:]
            #             stripped.append(content)
            #         else:
            #             stripped.append(line)
                
            #     paragraphs: list[str] = []
            #     current_para: list[str]  = []
                
            #     for line in stripped:
            #         if line.strip() == "":
            #             if current_para:
            #                 paragraphs.append(" ".join(current_para))
            #                 current_para = []
            #         else:
            #             current_para.append(line.strip())
                
            #     if current_para:
            #         paragraphs.append(" ".join(current_para))
                
            #     quote_children = []
            #     for para in paragraphs:
            #         quote_children.append(
            #             ParentNode(
            #                 tag="p",
            #                 children=text_to_children(para),
            #             )
            #         )
            #     html_children.append(
            #         ParentNode(
            #             tag="blockquote",
            #             children=quote_children,
            #         )
            #     )