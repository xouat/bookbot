def get_book_text(book_path):
    with open(book_path) as book:
        file_contents = book.read()
        return file_contents

def get_num_words(book_path):
    text = get_book_text(book_path)
    words = text.split()
    print(f"{len(words)} words found in the document")

def count_chars(book_path):
    char = None
    text = get_book_text(book_path)
    chars = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0
    }
    for i in range(0, len(text)):
        char = text[i].lower()
        if char in chars:
            chars[char] += 1
    print(chars)
        # chars[char] += 1
        # print(chars)
    
