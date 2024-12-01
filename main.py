def get_char_list(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_info = {"char": char, "num": char_dict[char]}
            char_list.append(char_info)
    return char_list

def sort_dict(dict):
    return dict["num"]


def count_char(_book):
    lowercase = _book.lower()
    dictionary = {}
    for char in lowercase:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] +=1
    return dictionary


def count_words(_book):
    text = str(_book)
    words = text.split() #returns a list (array) of words in the book
    return len(words)
    


def main():
    print("---Begin report of books/frankenstein.txt---")
    with open("books/frankenstein.txt") as f:
        print("File opened successfully")
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_count = count_char(file_contents)
    char_list = get_char_list(char_count)
    char_list.sort(reverse=True, key = sort_dict)
    print(f"{word_count} words found in the document\n")
    for char_dict in char_list:
        print(f"The '{char_dict["char"]}' character was found {char_dict["num"]} times")
    print ("--- End report---")
main()