def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        m1 = [[1,   2],[30, 40],]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        m2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9],]
        >>> sum_up_diagonals(m2)
        30
    """    
    total = 0

    # created a new list of values from top-left to bottom-right
    tl_br = [matrix[i][i] for i in range(len(matrix))]
    # iteration through the new list to add each value to 'total'
    for num in tr_bl:
        total = total + num
    
    # created a new list of values from bottom-left to top-right
    bl_tr = [matrix[i][len(matrix)-1-i] for i in range(len(matrix))]
    # iteration through the new list to add each value to 'total'
    for num in bl_tr:
        total = total + num
        
    print(total)