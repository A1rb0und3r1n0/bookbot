from stats import get_book_text
from stats import count_words
from stats import count_characters
from stats import split_dict
from stats import sort_on
import sys

characters = {}

def main():

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        count_characters(characters, filepath)
        sorted_characters = split_dict(characters)
        sorted_characters.sort(reverse=True, key=sort_on)

        print("============ BOOKBOT ============")
        print("Analyzing book found at " f"{filepath}" "...")
        print("----------- Word Count ----------")
        word_count = count_words(get_book_text(filepath))
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for index, dict in enumerate(sorted_characters):
            print(str(dict["char"]) + ": " + str(dict["num"]))
        print("============= END ===============")
    
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()