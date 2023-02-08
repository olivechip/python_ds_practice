def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_list = 'aeiou'
    vowel_freq = {}
    for letter in phrase:
        if letter.casefold() in vowel_list:
            if vowel_freq.get(letter.casefold()):
                vowel_freq[letter.casefold()] = vowel_freq[letter.casefold()] + 1
            else: 
                vowel_freq[letter.casefold()] = 1
    return vowel_freq