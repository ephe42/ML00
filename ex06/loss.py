#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import numpy as np


def loss_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (y_pred - y)^2 of the loss function.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    J_elem: numpy.array, a vector of dimension (number of the training examples,1).
    None if there is a dimension matching problem between y and y_hat.
    None if y or y_hat is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    if (
        isinstance(y, np.ndarray)
        and y.size != 0
        and isinstance(y_hat, np.ndarray)
        and y_hat.size != 0
        and y.shape == y_hat.shape
        and y.shape[1] == 1
    ):
        return np.array([(y_hat[i] - y[i]) * (y_hat[i] - y[i]) for i in range(len(y))])
    return


def loss_(y, y_hat):
    """
    Description:
    Calculates the value of loss function.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    J_value : has to be a float.
    None if there is a shape matching problem between y or y_hat.
    None if y or y_hat is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    if (
        isinstance(y, np.ndarray)
        and y.size != 0
        and isinstance(y_hat, np.ndarray)
        and y_hat.size != 0
        and y.shape == y_hat.shape
        and y.shape[1] == 1
    ):
        loss = np.square(y_hat - y).sum() / (2 * y.shape[0])
        return loss
    return


from prediction import predict_

if __name__ == "__main__":
    x1 = np.array([[0.0], [1.0], [2.0], [3.0], [4.0]])
    theta1 = np.array([[2.0], [4.0]])
    y_hat1 = predict_(x1, theta1)
    y1 = np.array([[2.0], [7.0], [12.0], [17.0], [22.0]])

    print(loss_elem_(y1, y_hat1))
    # Output: array([[0.0], [1], [4], [9], [16]])

    print(loss_(y1, y_hat1))
    # Output: 3.0

    x2 = np.array(
        [[0.2, 2.0, 20.0], [0.4, 4.0, 40.0], [0.6, 6.0, 60.0], [0.8, 8.0, 80.0]]
    )
    theta2 = np.array([[0.05], [1.0], [1.0], [1.0]])
    y_hat2 = predict_(x2, theta2)
    y2 = np.array([[19.0], [42.0], [67.0], [93.0]])

    print(loss_elem_(y2, y_hat2))
    # Output: array([[10.5625], [6.0025], [0.1225], [17.2225]])

    print(loss_(y2, y_hat2))
    # Output: 4.238750000000004

    x3 = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
    theta3 = np.array([[0.0], [1.0]])
    y_hat3 = predict_(x3, theta3)
    y3 = np.array([[2], [14], [-13], [5], [12], [4], [-19]])

    print(loss_(y3, y_hat3))
    # Output: 2.142857142857143

    print(loss_(y3, y3))
    # Output: 0.0
