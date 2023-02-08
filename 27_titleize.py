def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_list = phrase.split(' ')
    new_caps_list = [word.capitalize() for word in new_list]
    return (' ').join(new_caps_list)