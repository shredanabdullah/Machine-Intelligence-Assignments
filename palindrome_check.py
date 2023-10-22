import utils

def palindrome_check(string: str) -> bool:
    '''
    This function takes a string and returns whether it's a palindrome or not.
    A palindrome is a string that reads the same forwards and backward.
    Assume that empty strings are palindromes.
    '''
    count = len(string)
    
    for i in range(len(string)):
        if string[i] != string[count - 1]:
            return False  # Not a palindrome
        count -= 1

    if count == 0:
        return True  # It's a palindrome
    else:
        return False  # Not a palindrome

# same implementation in c because i'm more familier with it so i think in c then translate it to python until i got used to python.
# int palindrome_check(int* str) {
#     int count = 0;
#     int i;

#     for (i = 0; str[i] != '\0'; i++) {
#         count++;
#     }

#     count = count - 1;

#     for (i = 0; i < count; i++) {
#         if (str[i] != str[count]) {
#             return 0;
#         }
#         count--;
#     }

#     if (count == 0)
#         return 1;
#     else
#         return 0;
# }

