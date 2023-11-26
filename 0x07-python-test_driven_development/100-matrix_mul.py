#!/usr/bin/python3
"""..."""


def matrix_mul(m_a, m_b):
    """"..."""

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(val, int) or isinstance(val, float))
               for val in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(val, int) or isinstance(val, float))
               for val in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invrtB = []
    for i in range(len(m_b[0])):
        nRow = []
        for j in range(len(m_b)):
            nRow.append(m_b[j][i])
        invrtB.append(nRow)

    sum_m = []
    for row in m_a:
        nRow = []
        for col in invrtB:
            prod = 0
            for i in range(len(invrtB[0])):
                prod += row[i] * col[i]
            nRow.append(prod)
        sum_m.append(nRow)

    return sum_m
