import sys
from stats import *

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if not len(sys.argv) > 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    rel_file = sys.argv[1]
    print(f"Analyzing book found at {rel_file}...")
    content = get_book_text(rel_file)
    print("----------- Word Count ----------")
    print(f"Found {get_words_in_book(content)} total words")
    print("--------- Character Count -------")
    all_char = list_sort_dict(get_chars_in_book(content))
    for item in all_char:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")
main()