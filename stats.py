def word_count(text):
    word_count = 0
    for w in text.split():
        word_count += 1
    return word_count

def character_appearance(text):
    char_dict = {}
    for c in text.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict 

