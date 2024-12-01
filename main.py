def get_char_list(char_dict):   #takes a dictionary 
    char_list = []              #creates a list 
    for char in char_dict:      #for each char key in the dictionary we passed 
        if char.isalpha():      #if the key is a letter
            char_info = {"char": char, "num": char_dict[char]}  #create a var char_info thats a dict and make two key value pairs, grabbing the count for the char from the og dict
            char_list.append(char_info)                         #append this dictionary entry to the list char_info
    return char_list                                            #return the list after all is appended        

def sort_dict(dict):
    return dict["num"]      #using the key "num", we can look up how many char there are (see above for num establishment)


def count_char(_book):          #takes a string
    lowercase = _book.lower()   #converts all the chars to lowercase 
    dictionary = {}             #create a dictionary 
    for char in lowercase:      #for each character in the lowercase str
        if char not in dictionary:  #if the character is not in our dictionary already, add it as the key and set 1 as the value 
            dictionary[char] = 1
        else:                       #otherwise, increase the value that corresponds to that key by 1
            dictionary[char] +=1
    return dictionary               #return the dictionary 


def count_words(_book):     
    text = str(_book)
    words = text.split() #returns a list (array) of words in the book
    return len(words)
    


def main():
    print("---Begin report of books/frankenstein.txt---")
    with open("books/frankenstein.txt") as f:       #assign the file to variable f       
        file_contents = f.read()                    #store the contents of the file as a str in variable file_contents      
    word_count = count_words(file_contents)         #returns the total word count in our file
    char_count = count_char(file_contents)          #returns a dictionary with each character as key and count as value
    char_list = get_char_list(char_count)           #returns a list of dictionary entries 
    char_list.sort(reverse=True, key = sort_dict)   #key applies the function its set as to each item in the iterable and returns a value that is used as the sort key 
    print(f"{word_count} words found in the document\n")
    for char_dict in char_list:                     #for each dictionary entry in the char_list we've created (and sorted)
        print(f"The '{char_dict["char"]}' character was found {char_dict["num"]} times")    #print this statement with an f string 
    print ("--- End report---")
main()