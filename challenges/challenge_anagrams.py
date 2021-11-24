from helpers.anagrams_helper import sort_word

def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    
    if len(first_string) != len(second_string):
        return False
    
    
    if sort_word(first_string) == sort_word(second_string):
        return True
    
    return False