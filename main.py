from stats import count_words, count_all_chars

def get_books_text(path_to_file):
    with open(path_to_file) as book_file:
        return book_file.read()

def main():
    # print(get_books_text('./books/frankenstein.txt'))
    frankenstein_book_text = get_books_text('./books/frankenstein.txt')
    num_words_frankenstein = count_words(frankenstein_book_text)
    print(f"Found {num_words_frankenstein} total words")

    dict_of_words_frankenstein = count_all_chars(frankenstein_book_text)
    print(dict_of_words_frankenstein)

main()
