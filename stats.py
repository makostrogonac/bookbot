def count_words(book):
    list_of_words = book.split()
    return len(list_of_words)

def count_characters(book):
    letter_dict = {}
    letter_list = []
    list_of_words = book.split()
    for word in list_of_words:
        for letter in word:
            if letter.lower() not in letter_list:
                letter_list.append(letter.lower())
            lower_letter = letter.lower()
            if lower_letter in letter_dict:
                letter_dict[lower_letter] += 1 
            else:
                letter_dict[lower_letter] = 1
            letter_dict
    final_list = []
    counter = 0
    for letter in letter_list:
        dikt = dict()
        dikt["char"] = letter 
        dikt["num"] = letter_dict[letter]
        counter += 1
        final_list.append(dikt)
    return final_list
    
