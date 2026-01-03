def count_words(book_text):
    return len(book_text.split())

def count_all_chars(book_text):
    dict_chars = {}
    for char in book_text:
        char_lower = char.lower()
        if char_lower in dict_chars:
            dict_chars[char_lower] += 1
        else:
            dict_chars[char_lower] = 1
    return dict_chars

def get_ordered_char_freq_list(dict_chars):
    char_freq_list = []
    for char in dict_chars:
        char_freq_list.append({"char": char, "num": dict_chars[char]})
    char_freq_list.sort(reverse=True, key=lambda items: items["num"])
    return char_freq_list