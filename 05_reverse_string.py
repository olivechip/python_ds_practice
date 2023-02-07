def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    letters = [letter for letter in phrase]
    letters.reverse()
    return "".join(letters)