from stats import count_words, count_characters, count_characters_list
def get_book_text(path):
    with open(path) as f:
        file_contents =  f.read()
        return file_contents

def main():
    book = get_book_text("./books/frankenstein.txt")
    letters_count = count_characters(book)
    print(letters_count)
    
main()
