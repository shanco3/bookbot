from stats import word_count, character_appearance

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    char_instance = character_appearance(text)
    print(f"{word_count(text)} words found in the document")
    print(char_instance)
main()
