def saddle_points(matrix):
    check_matrix(matrix)
    saddle_point_set = set()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if j in get_max_indices(matrix[i]) and i in get_min_indices(get_matrix_col(matrix, j)):
                saddle_point_set.add((i, j))
    return saddle_point_set

def check_matrix(matrix):
    if len(matrix) > 0:
        for row in matrix:
            if len(row) != len(matrix[0]):
                raise ValueError('Invalid matrix')

def get_min_indices(vector):
    return [i for i, x in enumerate(vector) if x == min(vector)]

def get_max_indices(vector):
    results = [i for i, x in enumerate(vector) if x == max(vector)]
    return results

def get_matrix_col(matrix, col):
    column = []
    for row in matrix:
        column.append(row[col])
    return column
