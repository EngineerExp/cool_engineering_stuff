from block_to_html import markdown_to_html_node
import os
from generate_page import generate_page

def extract_title(markdown):
    """
    Extracts the title from a markdown string.
    The title is assumed to be the first line that starts with '# '.

    Args:
        markdown (str): The markdown content as a string.

    Returns:
        str: The extracted title, or an empty string if no title is found.
    """
    for line in markdown.splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("No h1 (# ...) title found in the markdown content. Make sure a space is between # and the title.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    """
    Recursively generates static HTML pages from markdown files in a directory and makes the same directory structure in the destination as needed.

    Args:
        dir_path_content (str): Path to the source directory containing markdown files.
        template_path (str): Path to the HTML template file.
        dest_dir_path (str): Path to the destination directory to save generated HTML files.
    """
    # list all directories in the source directory
    dest_list = os.listdir(dir_path_content)

    for item in dest_list:
        item_path = os.path.join(dir_path_content, item)
        dest_item_path = os.path.join(dest_dir_path, item)

        if os.path.isdir(item_path):
            # If the item is a directory, create the corresponding directory in the destination
            if not os.path.exists(dest_item_path):
                os.makedirs(dest_item_path, exist_ok=True)
            # Recursively process the subdirectory
            generate_pages_recursive(item_path, template_path, dest_item_path, basepath)
        elif item.endswith('.md'):
            # If the item is a markdown file, generate the HTML page
            dest_html_path = os.path.splitext(dest_item_path)[0] + '.html'
            generate_page(item_path, template_path, dest_html_path, basepath)