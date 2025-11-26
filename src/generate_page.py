from block_to_html import markdown_to_html_node
import os

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

# function to generate a static HTML page from markdown using a template
def generate_page(from_path, template_path, dest_path, basepath):
    """
    Generates a static HTML page from a markdown file using a template.

    Args:
        from_path (str): Path to the source markdown file.
        template_path (str): Path to the HTML template file.
        dest_path (str): Path to save the generated HTML file.
    """
    # Print that we are generating the page
    print(f"Generating page from \n{from_path} to \n{dest_path} using template \n{template_path}")

    # Read the markdown content
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Read the template content
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract title
    title = extract_title(markdown_content)

    # Replace placeholders in the template
    final_html = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)
    final_html = final_html.replace('href="/',f'href="{basepath}').replace('src="/',f'src="{basepath}')

    # make sure the destination directory exists
    directory = os.path.dirname(dest_path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    # Write the final HTML to the output path
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
   

if __name__ == "__main__":
    # Example usage of extract_title
    print(extract_title("# My First Static Website\nThis is a sample markdown content."))