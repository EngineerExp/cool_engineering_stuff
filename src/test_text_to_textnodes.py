import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_simple_bold(self):
        text = "This is **bold** text."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_italic_and_code(self):
        text = "This is _italic_ and `code`."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_image_and_link(self):
        text = "Here is an ![alt text](http://image.url) and a [link](http://link.url)."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, url="http://image.url"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, url="http://link.url"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)