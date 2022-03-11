#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import numpy as np


class TinyStatistician:
    def mean(self, x):
        if len(x) > 0:
            return float(
                sum([x[i] for i in range(len(x)) if not np.isnan(x[i])]) / len(x)
            )

    def median(self, x):
        if len(x) > 0:
            tab = [x[i] for i in range(len(x)) if not np.isnan(x[i])]
            tab.sort()
            half = int(len(tab) / 2)
            if len(tab) % 2 != 0:
                return float(tab[half])
            return float((tab[half - 1] + tab[half]) / 2)

    def quartile(self, x):
        if len(x) > 0:
            tab = [x[i] for i in range(len(x)) if not np.isnan(x[i])]
            tab.sort()
            quarter = (len(tab) - 1) / 4
            down = np.floor(quarter)
            up = np.ceil(quarter)
            if down == up:
                first = tab[int(quarter)]
            else:
                first = tab[int(down)] * (up - quarter) + tab[int(up)] * (
                    quarter - down
                )
            quarter = ((len(tab) - 1) / 4) * 3
            down = np.floor(quarter)
            up = np.ceil(quarter)
            if down == up:
                third = tab[int(quarter)]
            else:
                third = tab[int(down)] * (up - quarter) + tab[int(up)] * (
                    quarter - down
                )
            return [float(first), float(third)]

    def percentile(self, x, p):
        if len(x) > 0:
            tab = [x[i] for i in range(len(x)) if not np.isnan(x[i])]
            tab.sort()
            return float(tab[int((p * len(tab)) / 100)])

    def var(self, x):
        if len(x) > 0:
            m = self.mean(x)
            var = sum(
                [(x[i] - m) * (x[i] - m) for i in range(len(x)) if not np.isnan(x[i])]
            )
            return float(var / (len(x)))

    def sqrt(self, x):
        diff = 1
        a = x
        if x <= 0:
            return 0
        while diff > 0.001:
            b = 0.5 * (a + x / a)
            diff = a - b
            a = b
        return a

    def std(self, x):
        if len(x) > 0:
            var = self.var(x)
            return float(self.sqrt(var))


if __name__ == "__main__":
    a = [1, 42, 300, 10, 59]
    stat = TinyStatistician()

    print(stat.mean(a))
    # Output: 82.4

    print(stat.median(a))
    # Output: 42.0

    print(stat.quartile(a))
    # Output: [10.0, 59.0]

    print(stat.percentile(a, 10))
    # Output: 1.0

    print(stat.percentile(a, 28))
    # Output: 10.0

    print(stat.percentile(a, 83))
    # Output: 300.0

    print(stat.var(a))
    # Output: 12279.4399

    print(stat.std(a))
    # Output: 110.8126
