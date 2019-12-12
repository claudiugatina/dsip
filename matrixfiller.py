import numpy as np
from scipy.spatial import Delaunay


def matrix_from_array(v, n, m):

    minx, maxx = min(v[i][0] for i in range(0, len(v))), max(v[i][0] for i in range(0, len(v)))
    miny, maxy = min(v[i][1] for i in range(0, len(v))), max(v[i][1] for i in range(0, len(v)))

    width = maxx - minx
    height = maxy - miny
    mat = np.array([[0 for i in range(0, m)] for j in range(0, n)])

    def coord_to_indice(x, y):
        i = int(((y - miny) / height) * (n - 1))
        j = int(((x - minx) / width) * (m - 1))
        return i, j

    for elem in v:
        x = elem[0]
        y = elem[1]
        i, j = coord_to_indice(x, y)
        i = int(((y - miny) / height) * (n - 1))
        j = int(((x - minx) / width) * (m - 1))

        # some refactoring might make the code clearer
        mat[i][j] = elem[2]

    points = [[elem[0], elem[1]] for elem in v]

    triangulation = Delaunay(points)

    for point_indices in triangulation.simplices:
        indices_in_matrix = []
        for indice in point_indices:
            x, y = points[indice]
            indices_in_matrix.append(coord_to_indice(x, y))

        indices_in_matrix.sort()
        first, second, third = indices_in_matrix[0], indices_in_matrix[1], indices_in_matrix[2]
        for i in range(first[0] + 1, second[0] + 1):
            y_to_second = int(first[1] + ((second[1] - first[1]) / (second[0] - first[0])) * (i - first[0]))
            y_to_third = int(first[1] + ((third[1] - first[1]) / (third[0] - first[0])) * (i - first[0]))

            for j in range(min(y_to_second, y_to_third), max(y_to_second, y_to_third) + 1):
                if mat[i][j] != 0:
                    continue
                invdist = [1 / np.sqrt((i - ind[0]) ** 2 + (j - ind[1]) ** 2) for ind in indices_in_matrix]
                mat[i][j] = sum(
                    invdist[i] * mat[indices_in_matrix[i][0]][indices_in_matrix[i][1]] for i in range(0, 3)) / sum(
                    invdist)
                
        for i in range(second[0] + 1, third[0]):
            y_to_first = int(first[1] + ((third[1] - first[1]) / (third[0] - first[0])) * (i - first[0]))
            y_to_second = int(second[1] + ((third[1] - second[1]) / (third[0] - second[0])) * (i - second[0]))

            for j in range(min(y_to_second, y_to_first), max(y_to_second, y_to_first) + 1):
                invdist = [1 / np.sqrt((i - ind[0]) ** 2 + (j - ind[1]) ** 2) for ind in indices_in_matrix]
                mat[i][j] = sum(invdist[i] * mat[indices_in_matrix[i][0]][indices_in_matrix[i][1]] for i in range(0, 3)) / sum(invdist)

    return mat