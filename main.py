import string
WORD_LENGTH = 5
#Import string and define word lenghth as 5

def read_dictionary(file_name):
    new_dictionary_list = []
    #open file to read the content in the file
    info_file = open(file_name)
    infos_in_file = info_file.readlines()
    for word in infos_in_file:
        #replace new_line with blank and makes the files words in lower case
        new_dictionary_list.append(word.replace('\n', '').lower())
        #close file
    info_file.close()
    return new_dictionary_list

#makes the user input a word in lower case
def enter_a_word(word_type, num_letters):
    input_the_word = input(f"Enter the {num_letters}-letter {word_type} word: ").lower()
    return input_the_word

#checking if the input is in the file(dictionary)
def is_it_a_word(input_word, dictionary_list):
    if input_word in dictionary_list:
        return True
    else:
        return False

#check if the user have entered a word that is on the dictionary
def enter_and_check(word_type, dictionary_list):
    while True:
        in_word = enter_a_word(word_type, WORD_LENGTH)
        if (len(in_word) != 5) and is_it_a_word(in_word, dictionary_list):
            print(f'\nYou entered a {len(in_word)}-letter word that is in the dictionary. Please try again!')
            continue
        if (len(in_word) != 5) and (not is_it_a_word(in_word, dictionary_list)):
            print(f"\nYou entered a {len(in_word)}-letter word that is not in the dictionary. Please try again!")
            continue
        return in_word.lower()

#compare word to see wather they are in the same spot, if not the letter in the place will be replaced by "___"
def compare_words(player, secret, secret_correct, secret_incorrect, no_secret, left_over):
    global remaining_alphabet
    global in_secret_word_correct_spot
    global in_secret_word_somewhere
    global not_in_secret_word
    final = ''
    in_correct_spot = 0
    secret_copy = list(secret)  # Make a copy of the secret word
    for i, letter in enumerate(player):
        if letter == secret_copy[i]:
            final += letter
            in_correct_spot += 1
            if letter not in secret_correct:
                secret_correct.append(letter)
            secret_copy[i] = None  # Mark the corresponding letter in the copy as None
        elif letter in secret_copy:
            final += '(' + letter + ')'
            if letter not in secret_incorrect:
                secret_incorrect.append(letter)
            secret_copy[secret_copy.index(letter)] = None  # Mark the corresponding letter in the copy as None
        else:
            if letter not in no_secret:
                no_secret.append(letter)
            final += '_'
        if letter in left_over:
            left_over.remove(letter)
    return final, in_correct_spot



print('Welcome to new and improved Wordle - CECS 174 edition!')

alphabet_string = string.ascii_lowercase #Create a string ofall lowercase letters

remaining_alphabet = list(alphabet_string) #Create a list ofall lowercase letters

in_secret_word_correct_spot = [] # a list of all charactersthat have been previously attempted that are in the secretword in the correct spot

in_secret_word_somewhere = [] # a list of all characters thathave been previously attempted that are in the secret wordbut not in the correct spot

not_in_secret_word = [] # a list of all characters that havebeen previously attempted but not in the secret

words_list = read_dictionary("/Users/enzomoro/Downloads/project4_dictionary.txt")#File on computer that is related of the dictionary

secret_word = enter_and_check("secret", words_list)

#Input the allowed attempts
N = int(input("Input allowed number of attempts: "))
attempts = 1
#If attempts are higher than N the process will finalize with the user being a Failure
if N > 0:
    print(f"Enter your attempt #{attempts}")
    player_word = enter_and_check('player', words_list)
    #While the attempts are still lower than N, give hints to player 2
    while attempts <= N:
        final_word, letter_in_the_right_spot = compare_words(player_word, secret_word, in_secret_word_correct_spot, in_secret_word_somewhere, not_in_secret_word, remaining_alphabet)
        print(f"\nletter in the right spot: {letter_in_the_right_spot}")
        print(f"You guessed letters of the secret_word: {final_word}")
        print(f"Previously attempted letters that are in the correct spot of secret_word:\n{in_secret_word_correct_spot}")
        print(f"Previously attempted letters that are in some spot of secret_word:\n{in_secret_word_somewhere}")
        print(f"Previously attempted letters that are not in the secret_word:\n{not_in_secret_word}")
        print(f"Remaining letters of the alphabet that have not been tried:\n{remaining_alphabet}")
#If player 2 gets the word correct he will be a winner
        if letter_in_the_right_spot == WORD_LENGTH:
            print(f"Congrats you won using {attempts} attempt(s)")
            break
#count attempts every loop, and show the player how many attempts he has
        attempts += 1
        if attempts >= (N + 1):
            print(f"You already used #{attempts - 1} attempts. Better luck tomorrow!")
        else:
            print(f"Enter your attempt #{attempts}")
            player_word = enter_and_check("player", words_list)


