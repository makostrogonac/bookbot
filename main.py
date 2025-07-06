from stats import count_characters, count_words
import sys

def sort_on(items):
    return items["num"]

def get_book_text(path):
    with open(path) as f:
        file_contents =  f.read()
        return file_contents


if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
text = get_book_text(path)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {count_words(text)} total words")
print("--------- Character Count -------")
result = count_characters(text)
result.sort(key=sort_on, reverse=True)
for letter in result:
    print(letter["char"] + ": " + str(letter["num"]))
