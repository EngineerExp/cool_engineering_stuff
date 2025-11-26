import unittest

from htmlnode import HTMLNode

class TestHTMLNodePropsToHTML(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), "")
    
    def test_single_prop(self):
        node = HTMLNode(tag="div", props={"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')
    
    def test_multiple_inputs(self):
        node = HTMLNode(tag="div",value="this text for test",children=["node1","node2"] , props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')
    

if __name__ == "__main__":
    unittest.main()