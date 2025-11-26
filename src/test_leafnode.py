import unittest

from htmlnode import LeafNode

class TestLeafNodeToHTML(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click here", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" target="_blank">Click here</a>')

    # def test_leaf_to_html_empty_value(self):
    #     node = LeafNode("span", "")
    #     self.assertEqual(node.to_html(), ValueError("LeafNode must have a value to convert to HTML"))
    

if __name__ == "__main__":
    unittest.main()