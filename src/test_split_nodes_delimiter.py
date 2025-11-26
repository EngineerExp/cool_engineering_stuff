import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_bold_delimiter(self):
        node = TextNode("Here is some **bold text** in between", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("Here is some ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in between", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_no_delimiter(self):
        node = TextNode("No special formatting here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [TextNode("No special formatting here", TextType.TEXT)]
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_multiple_delimiters(self):
        node = TextNode("Mixing `code` and **bold** text", TextType.TEXT)
        nodes_after_code_split = split_nodes_delimiter([node], "`", TextType.CODE)
        final_nodes = []
        for n in nodes_after_code_split:
            if n.text_type == TextType.TEXT:
                final_nodes.extend(split_nodes_delimiter([n], "**", TextType.BOLD))
            else:
                final_nodes.append(n)
        expected_nodes = [
            TextNode("Mixing ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(final_nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()