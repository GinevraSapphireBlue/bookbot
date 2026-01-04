from stats import count_words, count_all_chars, get_ordered_char_freq_list
import sys

def get_books_text(path_to_file):
    with open(path_to_file) as book_file:
        return book_file.read()

def print_report(path_to_file, num_words, char_frequency):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_freq in char_frequency:
        char, freq = char_freq.values()
        if char.isalpha():
            print(f"{char}: {freq}")
    print("============= END ===============")


def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    frankenstein_book_text = get_books_text(path_to_file)

    # Count words in the book
    num_words_frankenstein = count_words(frankenstein_book_text)
    # print(f"Found {num_words_frankenstein} total words")

    # Count repetitions of characters in book
    dict_of_words_frankenstein = count_all_chars(frankenstein_book_text)
    # print(dict_of_words_frankenstein)

    # Create ordered list of characters' frequency
    ordered_char_frequency = get_ordered_char_freq_list(dict_of_words_frankenstein)
    # print(ordered_char_frequency)

    # Print report about the book
    print_report(path_to_file, num_words_frankenstein, ordered_char_frequency)

main()
