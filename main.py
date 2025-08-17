from stats import get_num_words, list_chars
import sys

def print_list(book_path):
    char_list = list_chars(book_path)
    words = get_num_words(book_path)
    char_output = None
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")
    print("----------- Character Count ----------")
    for char in char_list:
        char_output= char["char"] + ": " + str(char["num"])
        print(char_output)
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        print(sys.argv[1])
        print_list(sys.argv[1])


main()