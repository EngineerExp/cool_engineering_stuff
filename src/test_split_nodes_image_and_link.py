from split_nodes_image_and_link import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

def test_split_links(self):
    node = TextNode(
        "This is text with a [link](https://example.com) and another [second link](https://example2.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example2.com"),
        ],
        new_nodes,
    )

def test_both_images_and_links(self):
    node = TextNode(
        "Here is an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
        TextType.TEXT,
    )
    nodes_after_image_split = split_nodes_image([node])
    final_nodes = []
    for n in nodes_after_image_split:
        final_nodes.extend(split_nodes_link([n]))
    
    self.assertListEqual(
        [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ],
        final_nodes,
    )

def test_no_images_or_links(self):
    node = TextNode(
        "This is just plain text with no images or links.",
        TextType.TEXT,
    )
    nodes_after_image_split = split_nodes_image([node])
    final_nodes = []
    for n in nodes_after_image_split:
        final_nodes.extend(split_nodes_link([n]))
    
    self.assertListEqual(
        [TextNode("This is just plain text with no images or links.", TextType.TEXT)],
        final_nodes,
    )