import sys
from stats import get_num_words, get_characters, sort_count



def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_format(word_count, sorted_count, path_to_book):
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_count:
        if char_dict['char'].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")


def argv_error():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    argv_error()
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    wc = get_num_words(book)
    cc = get_characters(book)
    sc = sort_count(cc)
    print_format(wc, sc, book_path)
    #print(sc)

main()
