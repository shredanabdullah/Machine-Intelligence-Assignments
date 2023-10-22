from typing import Tuple, List
import utils
from helpers.test_tools import read_text_file,read_word_list

'''
    The DecipherResult is the type defintion for a tuple containing:
    - The deciphered text (string).
    - The shift of the cipher (non-negative integer).
        Assume that the shift is always to the right (in the direction from 'a' to 'b' to 'c' and so on).
        So if you return 1, that means that the text was ciphered by shifting it 1 to the right, and that you deciphered the text by shifting it 1 to the left.
    - The number of words in the deciphered text that are not in the dictionary (non-negative integer).
'''
DechiperResult = Tuple[str, int, int]

def caesar_dechiper(ciphered: str, dictionary: List[str]) -> DechiperResult:
    result = ('', 0, float('inf'))#initiallyy
    dictionary_set = set(dictionary)

    for move in range(26):  
        decrypted_text = ''
        non_dict_words = 0
        for character in ciphered:
            if character == ' ':
                decrypted_text += ' '
            else:
                shifted_char = chr(((ord(character) - ord('a') - move) % 26) + ord('a'))
                decrypted_text += shifted_char
        words = decrypted_text.split()
        non_dict_words = sum(1 for word in words if word not in dictionary_set)
##finding best resultss
        # if non_dict_words == 0: ##->>>>not passing some test cases so i comment it
        #     return (decrypted_text, move, non_dict_words)

        if non_dict_words < result[2]:
            result = (decrypted_text, move, non_dict_words)

    return result



# def caesar_dechiper(ciphered: str, dictionary: List[str]) -> DechiperResult:
#     result = ('', 0, float('inf'))

#     for move in range(26):  # 26 possible moves or shifts
#         deciphered_text = decrypt_caesar(ciphered, move) ##->>>>decrypt_caesar() function to be implemented(lsa ha3mlhaa)
#         words = deciphered_text.split()
#         non_dict_words = sum(1 for word in words if word not in dictionary)

#         if non_dict_words < best_result[2]:
#             result = (deciphered_text, move, non_dict_words)

#     return result


# #def caesar_dechiper(ciphered: str, dictionary: List[str]) -> DechiperResult:
#     '''
#         This function takes the ciphered text (string)  and the dictionary (a list of strings where each string is a word).
#         It should return a DechiperResult (see above for more info) with the deciphered text, the cipher shift, and the number of deciphered words that are not in the dictionary. 
#     '''
    



