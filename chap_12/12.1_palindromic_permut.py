def is_palindromic_permutable(word):
    letter_frequency = {}
    for letter in word:
        letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
    
    sum_of_elements = 0
    for val in letter_frequency.values():
        sum_of_elements += val % 2
    return True if sum_of_elements <= 1 else False

word = 'level'
print(f"Word {word} is palindromic - {is_palindromic_permutable(word)} ")