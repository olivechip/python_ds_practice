def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if parens[0] == ')' or parens[len(parens)-1] == '(':
        return False
    if parens.count('(') != parens.count(')'):
        return False
    
    open_count = 1
    close_count = 0
    for char in parens:
        if char == '(':
            open_count = open_count + 1
        elif char == ')':
            close_count = close_count + 1
        if close_count > open_count:
            return False
    return True
