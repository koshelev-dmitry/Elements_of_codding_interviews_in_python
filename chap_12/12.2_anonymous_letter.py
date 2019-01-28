def is_constructable(letter_text, newspaper_text):
    from collections import Counter
    letter_stat = Counter(letter_text)

    for ch in newspaper_text:
        if ch in letter_stat:
            if letter_stat[ch] > 0:
                letter_stat[ch] -= 1
            else:
                del letter_stat[ch]
                if letter_stat == {}:
                    return True
    return False

def is_letter_constructable(letter_text, newspaper_text):
    from collections import Counter
    return Counter(letter_text) - Counter(newspaper_text) == {}
    
letter = 'Hello World!'
newspaper = 'Hello World and !'
print(is_letter_constructable(letter, newspaper))