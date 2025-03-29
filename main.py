import sys
from stats import get_num_words, get_character_occurrence


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

filepath = 'books/frankenstein.txt'
book_text = get_book_text(sys.argv[1])
num_words = get_num_words(book_text)

sorted_dict = get_character_occurrence(book_text)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("----------- Character Count ----------")
for key, value in sorted_dict.items():
    if key.isalpha():
        print(f"{key}: {value}")
print("============= END ===============")