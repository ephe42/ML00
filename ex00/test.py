#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

from matrix import Matrix, Vector

if __name__ == "__main__":
    m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
    print(m1.shape)
    # Output:
    # (3, 2)

    print(m1.T())
    # Output:
    # Matrix([[0., 2., 4.], [1., 3., 5.]])

    print(m1.T().shape)
    # Output:
    # (2, 3)

    print()

    m1 = Matrix([[0.0, 2.0, 4.0], [1.0, 3.0, 5.0]])
    print(m1.shape)
    # Output:
    # (2, 3)

    print(m1.T())
    # Output:
    # Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])

    print(m1.T().shape)
    # Output:
    # (3, 2)

    print()

    m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
    print(m1 * m2)
    # Output:
    # Matrix([[28., 34.], [56., 68.]])

    print()

    v1 = Vector([[1, 2, 3]])  # create a row vector
    print(v1)
    v2 = Vector([[1], [2], [3]])  # create a column vector
    print(v2)
    try:
        v3 = Vector([[1, 2], [3, 4]])  # return an error
    except ValueError as e:
        print("Wrong size detected")

    print()

    m1 = Matrix([[0.0, 1.0, 2.0], [0.0, 2.0, 4.0]])
    v1 = Vector([[1], [2], [3]])
    print(m1 * v1)
    # Output:
    #     Matrix([[8], [16]])

    v1 = Vector([[1], [2], [3]])
    v2 = Vector([[2], [4], [8]])
    print(v1 + v2)
    # Output:
    # Vector([[3],[6],[11]])
    # Or: Vector([[8], [16]

    print(v1.dot(v2))
