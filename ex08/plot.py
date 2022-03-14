#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def plot_with_loss(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    y: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a vector of shape 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exception.
    """
    if (
        isinstance(x, np.ndarray)
        and x.size != 0
        and x.shape[1] == 1
        and isinstance(y, np.ndarray)
        and y.size != 0
        and y.shape[1] == 1
        and isinstance(theta, np.ndarray)
        and theta.size != 0
        and theta.shape == (2, 1)
    ):
        predict = np.insert(x, 0, values=1.0, axis=1).astype(float)
        predict = predict @ theta
        cost = np.square(predict - y).sum() / y.shape[0]
        plt.title(f"Cost : {cost}")
        plt.scatter(x, y)
        plt.plot(x, predict, "r")
        plt.vlines(x, predict, y, linestyle="dashed", color="r")
        plt.show()
        return
    return


if __name__ == "__main__":
    x = np.arange(1, 6).reshape(-1, 1)
    y = np.array(
        [[11.52434424], [10.62589482], [13.14755699], [18.60682298], [14.14329568]]
    )

    theta1 = np.array([[18], [-1]])
    plot_with_loss(x, y, theta1)

    theta2 = np.array([[14], [0]])
    plot_with_loss(x, y, theta2)

    theta3 = np.array([[12], [0.8]])
    plot_with_loss(x, y, theta3)
