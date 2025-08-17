def get_book_text(book_path):
    with open(book_path) as book:
        file_contents = book.read()
        return file_contents

def get_num_words(book_path):
    text = get_book_text(book_path)
    words = text.split()
    #print(f"{len(words)} words found in the document")
    return words

def count_chars(book_path):
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
    for char in text:
        if char in chars:
            chars[char] += 1
    return chars

def new_count(book_path):
    text = get_book_text(book_path)
    chars = {}
    for char in text:
        if char.lower() not in chars:
            chars[char.lower()] = 1
        elif char.lower() in chars:
            chars[char.lower()] += 1
    return chars

def list_chars(bookpath):    
    chars = new_count(bookpath)
    new_chars = []
    entry = None
    for char in chars:
        if char.isalpha():
            entry = {
                "char": char,
                "num": chars[char]
            }
            new_chars.append(entry)
    def get_char_count(i):
        return i["num"]
    new_chars.sort(key=get_char_count, reverse=True)
    return new_chars
