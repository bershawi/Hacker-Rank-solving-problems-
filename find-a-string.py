def count_substring(string, sub_string):
    letter_number = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            letter_number += 1
    return letter_number
