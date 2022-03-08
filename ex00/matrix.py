#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-


class Vector:
    def __init__(self, args):
        self.values = []
        self.shape = (0, 0)
        if args and isinstance(args, list):
            self.values = args
            self.shape = (1, len(self.values))
            if isinstance(self.values[0], list):
                self.shape = (len(self.values), len(self.values[0]))
        elif isinstance(args, int) and args > 0:
            for i in range(0, args):
                self.values.append([float(i)])
            self.shape = (args, 1)
        elif (
            isinstance(args, tuple)
            and len(args) == 2
            and isinstance(args[0], int)
            and isinstance(args[1], int)
        ):
            if args[0] == args[1] or args[0] > args[1]:
                raise ValueError("invalid args")
            for i in range(args[0], args[1]):
                self.values.append([float(i)])
            self.shape = (len(self.values), 1)
        else:
            raise ValueError("invalid args")

    def full(self, shape, fill_value):
        try:
            if shape[0] == 1:
                matrix = [fill_value for x in range(shape[1]) for y in range(shape[0])]
            else:
                matrix = [
                    [fill_value for x in range(shape[1])] for y in range(shape[0])
                ]
            return Vector(matrix)
        except:
            raise ValueError("shape must be a tuple")

    def __add__(self, args):
        res = []
        if self.values:
            if args and isinstance(args, Vector):
                if self.shape == args.shape:
                    res = self.full(self.shape, 0)
                    if self.shape[0] == 1:
                        for i in range(0, self.shape[1]):
                            res.values[i] = self.values[i] + args.values[i]
                    else:
                        for i in range(0, self.shape[0]):
                            for j in range(0, self.shape[1]):
                                res.values[i][j] = self.values[i][j] + args.values[i][j]
                else:
                    raise ValueError("vectors don't have the same shape")
            else:
                raise TypeError("args must be vector")
        else:
            raise ValueError("vector is empty")
        return res

    def __radd__(self, args):
        res = []
        if self.values:
            if args and isinstance(args, Vector):
                if self.shape == args.shape:
                    res = self.full(self.shape, 0)
                    if self.shape[0] == 1:
                        for i in range(0, self.shape[1]):
                            res.values[i] = args.values[i] + self.values[i]
                    else:
                        for i in range(0, self.shape[0]):
                            for j in range(0, self.shape[1]):
                                res.values[i][j] = args.values[i][j] + self.values[i][j]
                else:
                    raise ValueError("vectors don't have the same shape")
            else:
                raise TypeError("args must be vector")
        else:
            raise ValueError("vector is empty")
        return res

    # add : only vectors of same dimensions.
    def __sub__(self, args):
        res = []
        if self.values:
            if args and isinstance(args, Vector):
                if self.shape == args.shape:
                    res = self.full(self.shape, 0)
                    if self.shape[0] == 1:
                        for i in range(0, self.shape[1]):
                            res.values[i] = self.values[i] - args.values[i]
                    else:
                        for i in range(0, self.shape[0]):
                            for j in range(0, self.shape[1]):
                                res.values[i][j] = self.values[i][j] - args.values[i][j]
                else:
                    raise ValueError("vectors don't have the same shape")
            else:
                raise TypeError("args must be vector")
        else:
            raise ValueError("vector is empty")
        return res

    def __rsub__(self, args):
        res = []
        if self.values:
            if args and isinstance(args, Vector):
                if self.shape == args.shape:
                    res = self.full(self.shape, 0)
                    if self.shape[0] == 1:
                        for i in range(0, self.shape[1]):
                            res.values[i] = args.values[i] - self.values[i]
                    else:
                        for i in range(0, self.shape[0]):
                            for j in range(0, self.shape[1]):
                                res.values[i][j] = args.values[i][j] - self.values[i][j]
                else:
                    raise ValueError("vectors don't have the same shape")
            else:
                raise TypeError("args must be vector")
        else:
            raise ValueError("vector is empty")
        return res

    # sub : only vectors of same dimensions.
    def __truediv__(self, args):
        res = []
        try:
            args = float(args)
            res = self.full(self.shape, 0)
            if self.shape[0] == 1:
                for i in range(0, self.shape[1]):
                    res.values[i] = self.values[i] / args
            else:
                for i in range(0, self.shape[0]):
                    for j in range(0, self.shape[1]):
                        res.values[i][j] = self.values[i][j] / args
        except:
            raise TypeError("args must be scalar not null")
        return res

    def __rtruediv__(self, args):
        raise ValueError("A scalar cannot be divided by a Vector")

    # div : only scalars.
    def __mul__(self, args):
        res = []
        try:
            args = float(args)
            res = self.full(self.shape, 0)
            if self.shape[0] == 1:
                for i in range(0, self.shape[1]):
                    res.values[i] = self.values[i] * args
            else:
                for i in range(0, self.shape[0]):
                    for j in range(0, self.shape[1]):
                        res.values[i][j] = self.values[i][j] * args
        except:
            raise TypeError("args must be scalar")
        return res

    def __rmul__(self, args):
        res = []
        try:
            args = float(args)
            res = self.full(self.shape, 0)
            if self.shape[0] == 1:
                for i in range(0, self.shape[1]):
                    res.values[i] = args * self.values[i]
            else:
                for i in range(0, self.shape[0]):
                    for j in range(0, self.shape[1]):
                        res.values[i][j] = args * self.values[i][j]
        except:
            raise TypeError("args must be scalar")
        return res

    # mul : only scalars.
    def __str__(self):
        return f"{self.values}"

    def __repr__(self):
        return str(self)

    def dot(self, args):
        res = 0
        try:
            tmp = self
            if self.shape[0] != 1:
                tmp = self.T()
            if args.shape[0] != 1:
                args = args.T()
            for i in range(0, tmp.shape[1]):
                res += tmp.values[i] * args.values[i]
        except:
            raise TypeError("must be vectors of the same shape")
        return res

    def T(self):
        res = []
        try:
            res = self.full((self.shape[1], self.shape[0]), 0)
            if self.shape[0] == 1:
                for i in range(0, self.shape[0]):
                    for j in range(0, self.shape[1]):
                        res.values[j][i] = self.values[j]
            elif self.shape[1] == 1:
                for i in range(0, self.shape[0]):
                    for j in range(0, self.shape[1]):
                        res.values[i] = self.values[i][j]
            else:
                for i in range(0, self.shape[0]):
                    for j in range(0, self.shape[1]):
                        res.values[j][i] = self.values[i][j]
        except:
            raise ValueError("vector is empty")
        return res
