import unittest
from block_to_html import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# Heading 1
```
This is text that _should_ remain
the **same** even with inline stuff
```
## Heading 2
Some paragraph text.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre><h2>Heading 2</h2><p>Some paragraph text.</p></div>",
        )

    def test_code(self):
        md = """
Here is some
```
code
```
within a paragraph.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Here is some</p><pre><code>code\n</code></pre><p>within a paragraph.</p></div>",
        )
    
    def test_mixed_content(self):
        md = """ 
# THIS IS A HEADING
This is a paragraph with **bold** text.
```
This is a code block with _italic_ text.
```
> This is a quoted text with `code`.

Another paragraph here.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>THIS IS A HEADING</h1><p>This is a paragraph with <b>bold</b> text.</p><pre><code>This is a code block with _italic_ text.\n</code></pre><blockquote>This is a quoted text with <code>code</code>.</blockquote><p>Another paragraph here.</p></div>",
        )

if __name__ == "__main__":
    unittest.main()