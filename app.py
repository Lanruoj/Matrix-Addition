def add_matrix(m1,m2):
    if len(m1) and type(m1[0])==list:
        if (len(m1)!=len(m2)) or (len(m1[0])!=len(m2[0])):
            return None
        for col in range(0, len(m1)):
            for row in range(0, len(m1[0])):
                m1[col][row] += m2[col][row]
    else:
        if len(m1)!=len(m2):
            return None
        for i in range(0, len(m1)):
            m1[i] += m2[i]
    return m1

## TEST CASES ##

# matrixA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrixB = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

# matrixA = [1,1,1]
# matrixB = [1,1,1]

# matrixA = [1,1,1]
# matrixB = [1,1]
