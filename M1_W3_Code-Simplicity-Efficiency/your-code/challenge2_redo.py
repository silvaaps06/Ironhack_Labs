import string
import random

def string_generator(min_length, max_length, string_num):

#Creates a list with all lowercase letters of the alphabet
    letters = list(string.ascii_lowercase)

#Creates a list with the numbers 1-9 as characters or string
    numbers = [str(element) for element in range(0,10)]

#joining the two lists that will be where each character will be taken from
    list_numbers = letters + numbers

    words_list = []

#As long as the length of the list is less than the number of words requested from the user, words will continue to be added
    while len(words_list) < string_num:
        s = ""
        #Chosing a random number between the min and the max that the user entered and this number will be the length of that word
        string_length = random.randint(min_length, max_length + 1)

        #As long as the length of the new word is less than the Random number, characters will continue to be added
        while len(s) < string_length:
            s += random.choice(list_numbers)
        #Once all the characters for a word have been added, that word will be added to the list
        words_list.append(s)
        
    print(words_list)
    
string_generator(5,20,10)