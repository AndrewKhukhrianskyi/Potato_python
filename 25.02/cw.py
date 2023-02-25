def remove_consecutive_duplicates(s):
    list_text = s.split() 
    substrings = []
    substrings2 = []
    for word_index in range(len(list_text)):
        substring = ''
        for next_word_index in range(word_index, len(list_text)):
            if list_text[word_index] != list_text[next_word_index]:
                break
            substring += list_text[next_word_index] + ' '
        substrings.append(substring)
    
    for substring in substrings:
        sub = substring.strip().split()
        if len(sub) == 1:
            substrings2.append(sub[0])
    return ' '.join(substrings2)
