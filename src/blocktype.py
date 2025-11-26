
from enum import Enum

class BlockType(Enum):
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    PARAGRAPH = "paragraph"

def block_to_block_type(block_str: str) -> BlockType:
    
    # Check for heading
    count = 0
    i = 0
    while i < len(block_str) and block_str[i] == "#":
        count += 1
        i += 1
    if len(block_str) > count:
        if 1 <= count <= 6 and block_str[count] == " ":
            return BlockType.HEADING
    
    # split the block into lines for further checks
    lines = block_str.split("\n")
    
    # Check for code block
    if len(lines) > 1:
        if lines[0].strip() == "```" and lines[-1].strip() == "```":
            return BlockType.CODE
    
    # Check for blockquote
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Check for unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list
    number = 1
    ordered = True
    index = 0
    while index < len(lines) and ordered:
        line = lines[index]
        if not line.startswith(f"{number}. "):
            ordered = False
        number += 1
        index += 1
    if ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

if __name__ == "__main__":
    # Testing the block_to_block_type function
    test_blocks = [
        "# Heading 1",
        "## Heading 2",
        "``` \ncode line 1\ncode line 2\n```",
        "> This is a quote.\n> Another line of quote.",
        "- Item 1\n- Item 2\n- Item 3",
        "1. First item\n2. Second item\n3. Third item",
        "This is a simple paragraph."
    ]
    
    for block in test_blocks:
        block_type = block_to_block_type(block)
        print(f"Block:\n{block}\nType: {block_type}\n")