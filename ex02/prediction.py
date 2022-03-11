#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import numpy as np


def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a vector of shape 2 * 1.
    Returns:
    y_hat as a numpy.array, a vector of shape m * 1.
    None if x or theta are empty numpy.array.
    None if x or theta shapes are not appropriate.
    None if x or theta is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    if (
        isinstance(x, np.ndarray)
        and x.size != 0
        and x.shape[1] == 1
        and isinstance(theta, np.ndarray)
        and theta.size != 0
        and theta.shape == (2, 1)
    ):
        return np.array([theta[0] + theta[1] * i for i in x]).astype(float)
    return


if __name__ == "__main__":
    x = np.arange(1, 6).reshape(-1, 1)

    theta1 = np.array([[5], [0]])
    print(simple_predict(x, theta1))
    # Ouput: array([[5.],[5.],[5.],[5.],[5.]])

    theta2 = np.array([[0], [1]])
    print(simple_predict(x, theta2))
    # Output: array([[1.0], [2.0], [3.0], [4.0], [5.0]])

    theta3 = np.array([[5], [3]])
    print(simple_predict(x, theta3))
    # Output: array([[8.0], [11.0], [14.0], [17.0], [20.0]])

    theta4 = np.array([[-3], [1]])
    print(simple_predict(x, theta4))
    # Output: array([[-2.0], [-1.0], [0.0], [1.0], [2.0]])
