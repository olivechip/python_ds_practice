def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_list = [letter for letter in phrase]
    final_list = []
    for letter in phrase_list:
        if letter.casefold() == to_swap.casefold():
            letter = letter.swapcase()
        final_list.append(letter)
    return ('').join(final_list)
    
    