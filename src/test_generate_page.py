import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_with_valid_title(self):
        markdown = "# My First Static Website\nThis is a sample markdown content."
        expected_title = "My First Static Website"
        self.assertEqual(extract_title(markdown), expected_title)

    def test_extract_title_without_title(self):
        markdown = "This is a sample markdown content without a title."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("No h1 (# ...) title found", str(context.exception))

    def test_extract_title_with_no_space_after_hash(self):
        markdown = "#My First Static Website\nThis is a sample markdown content."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("No h1 (# ...) title found", str(context.exception))

    def test_extract_title_with_multiple_titles(self):
        markdown = "# First Title\nSome content.\n# Second Title\nMore content."
        expected_title = "First Title"
        self.assertEqual(extract_title(markdown), expected_title)

if __name__ == '__main__':
    unittest.main()