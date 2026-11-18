def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    len_a, len_b =  len(a), len(b)
    if len_a != len_b:
        return -1
    else:
        result = [0]*len_a
        for i in range(len_b):
            for j in range(len_a):
                result[i] += a[i][j]*b[j]
    return result
