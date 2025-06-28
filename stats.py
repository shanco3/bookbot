

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

def sort_on(char):
    return char["num"]

def sorter(char_dict):
    dict_list = []
    for k in char_dict:
        dict_list.append(dict([("char", k), ("num", char_dict[k])]))
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def printer(path, count, dicts):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {count} total words")
    print(f"--------- Character Count -------")
    for d in dicts:
        if d["char"].isalpha() == True:
            print(f"{d["char"]}: {str(d["num"])}")
    print(f"============= END ===============")
        