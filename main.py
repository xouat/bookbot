def get_book_text(book_path):
    with open(book_path) as book:
        file_contents = book.read()
        words = file_contents.split()
        print(f"{len(words)} words found in the document")

def main():
    get_book_text("books/frankenstein.txt")

main()