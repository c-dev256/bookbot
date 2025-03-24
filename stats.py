def get_words_in_book(file_contents):
    num_words = len(file_contents.split())
    return f"{num_words}"

def get_chars_in_book(file_contents):
    char_dict = {}
    for char in file_contents.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def list_sort_dict(dict):
    sorted_list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_list