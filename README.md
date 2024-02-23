Introduction
------------------------
This program takes in the letters of the daily New York Times Spelling Bee, and the primary letter in the middle. 

Word Finder Function
------------------------
The all_words function reads a txt file, and first takes in a list "modified_list" that has all the words with one of every given letter. It creates a second list "modified_list_1" that takes in all words with any of the letters, allowing for the storage of words with repeated letters. The third list "main_list" compiles the two, taking in all the words from modified_list and vetting out all the items in the "modified_list_1" that may not have the main letter.

Combinations Function
-----------------------
The all_words function is called for each combination of the letters. The function total_combinations finds all the combinations for the letters greater than length 3 but less than length 7, which is the total number of letters. In a for loop, each combination from the total_combinations function is passed through all_words, and is saved in final_list, where it is printed. 
