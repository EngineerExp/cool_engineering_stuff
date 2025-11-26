import os
import shutil
from generate_pages_recursive import generate_pages_recursive
import sys


def copy_src_to_dst(src_path, dst_path):
    # Ensure the destination directory exists
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    for item in os.listdir(src_path):
        src_item_path = os.path.join(src_path, item)
        dst_item_path = os.path.join(dst_path, item)

        if os.path.isfile(src_item_path) and not item.endswith('Zone.Identifier'):
            print(f"Copying file: \n{src_item_path} to \n{dst_item_path}")
            shutil.copy(src_item_path, dst_item_path)
        elif os.path.isdir(src_item_path):
            print(f"Entering directory:\n{src_item_path}")
            # Recursively call the function for subdirectories
            copy_src_to_dst(src_item_path, dst_item_path)

# ... (your main function setup) ...

def main():
    print("Welcome to My First Static Website Generator!")

    ## use sys.argv to change basepath
    basepath = "/"
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    elif len(sys.argv) > 2: # else, there are too many arguements
        raise Exception("use <main.py> for local generation or <main.py> '/path_to_repo/' to generate html for local use or repo/website use respectively")
    
    print(f"basepath  is: {basepath}")

    # delete {destination} directory if it exists
    destination = "docs"
    to_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f'{destination}')
    if os.path.exists(to_dir):
        print(f"Deleting existing destination directory: {to_dir}")
        shutil.rmtree(to_dir)

    # remake {destination} directory
    print(f"Creating {destination} directory: {to_dir}")
    os.makedirs(to_dir)

    # define source and destination directories
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_static_dir = os.path.join(project_root, 'static')
    dst_to_dir = os.path.join(project_root, f'{destination}')

    print(f"\nStarting copy from \n{src_static_dir} to \n{dst_to_dir}")
    copy_src_to_dst(src_static_dir, dst_to_dir)
    print("\nCopy process complete!\n")

    # reciursively generate pages from content markdown files to {destination} directory as html files
    from_path = os.path.join(project_root, 'content')
    template_path = os.path.join(project_root, 'template.html')
    dest_path = os.path.join(project_root, f'{destination}')
    generate_pages_recursive(from_path, template_path, dest_path, basepath)

    if basepath != "/":
        print(f'\nCommit to git repository and then check out the website! \nhttps://engineerexp.github.io{basepath} \n')


if __name__ == "__main__":
    main()