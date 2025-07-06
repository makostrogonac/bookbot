from stats import count_characters, count_characters_list

def sort_on(items):
    return items["num"]

def get_book_text(path):
    with open(path) as f:
        file_contents =  f.read()
        return file_contents
text = get_book_text("./books/frankenstein.txt")
result = count_characters_list(text)
print("started sorting")
result.sort(key=sort_on, reverse=False)
print(result)
