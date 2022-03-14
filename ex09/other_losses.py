#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import numpy as np


def mse_(y, y_hat):
    """
    Description:
    Calculate the MSE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
    mse: has to be a float.
    None if there is a matching shape problem.
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
        return np.square(y_hat - y).sum() / y.shape[0]
    return


def rmse_(y, y_hat):
    """
    Description:
    Calculate the RMSE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
    rmse: has to be a float.
    None if there is a matching shape problem.
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
        return np.sqrt(np.square(y_hat - y).sum() / y.shape[0])
    return


def mae_(y, y_hat):
    """
    Description:
    Calculate the MAE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
    mae: has to be a float.
    None if there is a matching shape problem.
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
        return abs(y_hat - y).sum() / y.shape[0]
    return


def r2score_(y, y_hat):
    """
    Description:
    Calculate the R2score between the predicted output and the output.
    Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
    Returns:
    r2score: has to be a float.
    None if there is a matching shape problem.
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
        return 1 - np.square(y_hat - y).sum() / np.square(y - np.mean(y)).sum()
    return


from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt

if __name__ == "__main__":
    x = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
    y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])

    print(mse_(x, y))
    # Output: 4.285714285714286
    print(mse_(x, y) == mean_squared_error(x, y))

    print(rmse_(x, y))
    # Output: 2.0701966780270626
    print(rmse_(x, y) == sqrt(mean_squared_error(x, y)))

    print(mae_(x, y))
    # Output: 1.7142857142857142
    print(mae_(x, y) == mean_absolute_error(x, y))

    print(r2score_(x, y))
    ## Output: 0.9681721733858745
    print(r2score_(x, y) == r2_score(x, y))
