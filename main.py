import sys
from stats import word_count, character_appearance, sorter, printer

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    char_dict = character_appearance(text)
    printer(book_path, word_count(text), sorter(char_dict))
main()
