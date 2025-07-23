def get_num_words(book_string):
    string_list = book_string.split()
    return len(string_list)


def get_characters(book_string):
    char_dictionary = {}

    current_book = book_string.lower()

    for character in current_book:

        if character.lower() in char_dictionary:
            char_dictionary[character.lower()] += 1

        else:
            char_dictionary[character.lower()] = 1

    return char_dictionary


def sort_count(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        temp_dict = {}
        temp_dict['char'] = key
        temp_dict['num'] = value
        dict_list.append(temp_dict)


    dict_list = sorted(dict_list, key=lambda d: d['num'])
    dict_list.reverse()

    return dict_list
