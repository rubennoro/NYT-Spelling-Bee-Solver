from itertools import combinations

letters = str(input('Please provide all the letters:')).lower()
print(f"You're letters are: {letters}")
#important_letter = str(input('Please provide the important letter')).lower()

main_letter = str(input('Please provide the center letter: '))

letter_list = list(letters)

#this will only take the panagrams
def all_words(filename, all_letters, main_letter):
    '''

    :param filename: name of the txt file passed through the function
    :param all_letters: the set of letters inputted by the user
    :param main_letter: the primary letter that each correct word must contain
    :return: list of the valid words under the combination size
    '''
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            words_list = file.read().splitlines()

    except FileNotFoundError:
        return 'Failure'

    modified_list = [word for word in words_list if all(letters in word for letters in all_letters)]
    # this takes all the words with, at the very least, the given letters

    modified_list_1 = [words for words in modified_list if any(letter not in all_letters for letter in words)]
    # this takes all the words with extra letters

    main_list = [item for item in modified_list if item not in modified_list_1 and main_letter in item]
    # this removes all words with extra letters from bigger list
    # this captures the panagram

    return main_list


def total_combinations(string, max_combos):
    '''

    :param string:
    :param max_combos: NYT's only takes in words of 4 letters or greater
    :return: recursively iterates to collect all the
    '''
    if max_combos <= 3:
        return []
    else:
        combos = [combo for combo in combinations(string, max_combos)]
    return combos + total_combinations(string, max_combos - 1)

lists = total_combinations(letters, 7)
# this prints as big list of individual combinations up to size 7, representing all the letters

filename = 'wordlist.txt'
final_list = []

for list in lists:
    if all_words(filename, list, main_letter):
        #assert that the list has content
        final_list.append(all_words(filename, list, main_letter))

flattened_final_list = [element for sublist in final_list for element in sublist]

print('The possible words are: ')
for final_word in flattened_final_list:
    print(final_word)
