def count_words(book):
    list_of_words = book.split()
    return len(list_of_words)

def count_characters(book):
    word_counter = 0
    list_of_words = book.split()
    for word in list_of_words:
        word_counter +=1
    return word_counter

def count_characters_list(book):
    letter_list = []
    print(not letter_list)
    list_of_words = book.split()
    word_count = 0
    for word in list_of_words:
        word_count += 1 
        print(word_count)
        for letter in word:
            word_dict = {"char": "", "num": 0}
            if not letter_list:
                word_dict["char"] = letter.lower()
                word_dict["num"] = 1
                letter_list.append(word_dict)
                break
            else:
                is_contained = 0
                for element in letter_list:
                    if element["char"] == letter.lower():
                        element["num"] += 1
                        is_contained = 1
                        break
                if is_contained:
                    word_dict["char"] = letter.lower()
                    word_dict["num"] = 1
                    letter_list.append(word_dict)
                    break
    return letter_list







