from string import ascii_lowercase as alc

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def count_characters(dict, path_to_file):

    book_text = get_book_text(path_to_file)
    removed_uppercase = book_text.lower()

    for char in removed_uppercase:
        if char in dict:
            dict[char] += 1
        else:   
            dict[char] = 1
    return dict

def split_dict(dict):

    characters_sorted = []

    for char in dict:
        if char.isalpha():
            characters_sorted.append({"char": char, "num": dict[char]})

    return characters_sorted

def sort_on(dict):
    return dict["num"]