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

def prompt_open_website(basepath,project_root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))):
    # Set the local URL based on the basepath (whether ./build.sh or ./main.sh was used)
    if basepath != "/": # then ./build.sh was used (for publishing to github pages)
        url = f'https://engineerexp.github.io{basepath}'
        print()
        print(f"Use following commands in another terminal to post to Github:\n(do commands within {project_root})\n\ngit add . \ngit commit -m 'your message' \ngit push origin main")

    else: # then ./main.sh was used (for local testing)
        url = 'http://localhost:8888/'

    asking = input(f"\nDo you want to open the website now? (y/n): ")
    if asking.lower() != 'y':
        print("Exiting without opening the website.")
        return
    else:
        import webbrowser
        from pathlib import Path
        # Attempt open the website in the Chrome browser on a new tab
        # This seems to only work if you specify the chrome path explicitly (note that /mnt/c/.. is for WSL to access windows C: drive)
        chrome_path = Path(r"/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe")
        if not os.path.exists(chrome_path):
            print("Cannot find Chrome.exe at specified path. Please update the path in the script to the Chrome.exe.")
        else:
            print(f'\n... Opening website... \n>>> Link: {url} \n')
            print(">>> Might need to refresh cache (ctrl + F5) to see updates\n")
            print(f"Opening Chrome from: {str(chrome_path)}")
            # open the local website in the chrome browser
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(str(chrome_path)))
            webbrowser.get('chrome').open(url, new=1, autoraise=True)

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

    # recursively generate pages from content markdown files to {destination} directory as html files
    from_path = os.path.join(project_root, 'content')
    template_path = os.path.join(project_root, 'template.html')
    dest_path = os.path.join(project_root, f'{destination}')
    generate_pages_recursive(from_path, template_path, dest_path, basepath)

    # recieve instructions (if applicable) and open website if prompted
    prompt_open_website(basepath, project_root)


if __name__ == "__main__":
    main()