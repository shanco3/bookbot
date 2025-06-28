from stats import word_count, character_appearance, sort_on, sorter, printer

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    char_dict = character_appearance(text)
    
    print(f'''
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count(text)} total words
--------- Character Count -------''')
    
    printer(sorter(char_dict))
    print(f"============= END ===============")

main()
