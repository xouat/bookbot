def get_book_text(book_path):
    with open(book_path) as book:
        file_contents = book.read()
        return file_contents

def get_num_words(book_path):
        text = get_book_text(book_path)
        words = text.split()
        print(f"{len(words)} words found in the document")