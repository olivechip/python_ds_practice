def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'AaEeIiOoUu'
    removed_list = [letter for letter in s if letter not in vowels]
    vowel_list = [letter for letter in s if letter in vowels]
    vowel_list.reverse()
    idx_list = []
    for i in range(len(s)):
        if s[i] in vowels:
            idx_list.append(i)
    # print(removed_list)
    # print(vowel_list)
    # print(idx_list)

    for i in range(len(vowel_list)):
        removed_list.insert(idx_list[i], vowel_list[i])
    final_str = ('').join(removed_list)
    print(final_str)
