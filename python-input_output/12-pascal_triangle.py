#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        previous_row = triangle[i-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(previous_row[j-1] + previous_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
