#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-


class Matrix:
    def __init__(self, args):
        self.data = []
        self.shape = (0, 0)
        if args and isinstance(args, list) and isinstance(args[0], list):
            self.data = args
            self.shape = (len(self.data), len(self.data[0]))
            for i in range(len(self.data)):
                if len(self.data[i]) != self.shape[1]:
                    raise ValueError("invalid shape")
                for j in self.data[i]:
                    if not isinstance(j, float) and not isinstance(j, int):
                        raise ValueError("matrix must only contain float or int")
        elif (
            isinstance(args, tuple)
            and len(args) == 2
            and isinstance(args[0], int)
            and isinstance(args[1], int)
        ):
            self.data = [[0.0 for j in range(args[1])] for i in range(args[0])]
            self.shape = args
        else:
            raise ValueError("invalid args")

    def full(self, shape, fill_value):
        try:
            if shape[0] == 1:
                matrix = [fill_value for x in range(shape[1]) for y in range(shape[0])]
                return Vector(matrix)
            else:
                matrix = [
                    [fill_value for x in range(shape[1])] for y in range(shape[0])
                ]
                return Matrix(matrix)
        except:
            raise ValueError("shape must be a tuple")

    # add : only matrices of same dimensions.
    def __add__(self, args):
        res = []
        if self.data:
            if args and isinstance(args, Matrix):
                if self.shape == args.shape:
                    res = self.full(self.shape, 0)
                    if self.shape[0] == 1:
                        for i in range(self.shape[1]):
                            res.data[i] = self.data[i] + args.data[i]
                    else:
                        for i in range(self.shape[0]):
                            for j in range(self.shape[1]):
                                res.data[i][j] = self.data[i][j] + args.data[i][j]
                else:
                    raise ValueError("matrix don't have the same shape")
            else:
                raise TypeError("args must be vector")
        else:
            raise ValueError("matrix is empty")
        return res

    def __radd__(self, args):
        res = []
        if self.data:
            if args and isinstance(args, Matrix):
                if self.shape == args.shape:
                    res = self.full(self.shape, 0)
                    if self.shape[0] == 1:
                        for i in range(self.shape[1]):
                            res.data[i] = args.data[i] + self.data[i]
                    else:
                        for i in range(self.shape[0]):
                            for j in range(self.shape[1]):
                                res.data[i][j] = args.data[i][j] + self.data[i][j]
                else:
                    raise ValueError("matrix don't have the same shape")
            else:
                raise TypeError("args must be matrix")
        else:
            raise ValueError("matrix is empty")
        return res

    # sub : only matrices of same dimensions.
    def __sub__(self, args):
        res = []
        if self.data:
            if args and isinstance(args, Matrix):
                if self.shape == args.shape:
                    res = self.full(self.shape, 0)
                    if self.shape[0] == 1:
                        for i in range(self.shape[1]):
                            res.data[i] = self.data[i] - args.data[i]
                    else:
                        for i in range(self.shape[0]):
                            for j in range(self.shape[1]):
                                res.data[i][j] = self.data[i][j] - args.data[i][j]
                else:
                    raise ValueError("matrix don't have the same shape")
            else:
                raise TypeError("args must be matrix")
        else:
            raise ValueError("matrix is empty")
        return res

    def __rsub__(self, args):
        res = []
        if self.data:
            if args and isinstance(args, Matrix):
                if self.shape == args.shape:
                    res = self.full(self.shape, 0)
                    if self.shape[0] == 1:
                        for i in range(self.shape[1]):
                            res.data[i] = args.data[i] - self.data[i]
                    else:
                        for i in range(self.shape[0]):
                            for j in range(self.shape[1]):
                                res.data[i][j] = args.data[i][j] - self.data[i][j]
                else:
                    raise ValueError("matrix don't have the same shape")
            else:
                raise TypeError("args must be matrix")
        else:
            raise ValueError("matrix is empty")
        return res

    def __truediv__(self, args):
        res = []
        try:
            args = float(args)
            res = self.full(self.shape, 0)
            if self.shape[0] == 1:
                for i in range(self.shape[1]):
                    res.data[i] = self.data[i] / args
            else:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        res.data[i][j] = self.data[i][j] / args
        except:
            raise TypeError("args must be scalar not null")
        return res

    def __rtruediv__(self, args):
        raise ValueError("A scalar cannot be divided by a matrix")

    def get_column(self, matrix):
        for i in range(matrix.shape[1]):
            ret = []
            for j in range(matrix.shape[0]):
                ret.append(matrix.data[j][i])
            yield ret

    def get_line(self, matrix):
        for i in range(matrix.shape[0]):
            yield matrix.data[i]

    # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
    # returns a Vector if we perform Matrix * Vector multiplication.
    def __mul__(self, args):
        res = []
        try:
            if self.shape[1] == args.shape[0]:
                # for l in self.get_line(self):
                #     tmp = []
                #     for c in self.get_column(args):
                #         tmp.append(sum([a * b for a, b in zip(l, c)]))
                #     res.append(tmp)
                res = [
                    [sum([a * b for a, b in zip(l, c)]) for c in self.get_column(args)]
                    for l in self.get_line(self)
                ]
        except:
            raise TypeError("args must be scalar")
        return res

    def __rmul__(self, args):
        res = []
        try:
            if self.shape[1] == args.shape[0]:
                res = [
                    [sum([a * b for a, b in zip(l, c)]) for c in self.get_column(args)]
                    for l in self.get_line(self)
                ]
        except:
            raise TypeError("args must be scalar")
        return res

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return str(self)

    def T(self):
        res = []
        try:
            res = self.full((self.shape[1], self.shape[0]), 0)
            if self.shape[0] == 1:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        res.data[j][i] = self.data[j]
            elif self.shape[1] == 1:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        res.data[i] = self.data[i][j]
            else:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        res.data[j][i] = self.data[i][j]
        except:
            raise ValueError("matrix is empty")
        return res


class Vector(Matrix):
    def __init__(self, args):
        self.data = []
        self.shape = (0, 0)
        if args and isinstance(args, list):
            self.data = args
            self.shape = (1, len(self.data))
            if isinstance(self.data[0], list):
                self.shape = (len(self.data), len(self.data[0]))
                for i in range(len(self.data)):
                    for j in self.data[i]:
                        if not isinstance(j, float) and not isinstance(j, int):
                            raise ValueError("matrix must only contain float or int")
        elif (
            isinstance(args, tuple)
            and len(args) == 2
            and isinstance(args[0], int)
            and isinstance(args[1], int)
        ):
            self.data = [[0.0 for j in range(args[1])] for i in range(args[0])]
            self.shape = args
        else:
            raise ValueError("invalid args")
        if self.shape[0] != 1 and self.shape[1] != 1:
            raise ValueError("must be vector and not matrix")

    def dot(self, args):
        res = 0
        try:
            tmp = self
            if self.shape[0] != 1:
                tmp = self.T()
            if args.shape[0] != 1:
                args = args.T()
            for i in range(tmp.shape[1]):
                res += tmp.data[i] * args.data[i]
        except:
            raise TypeError("must be vectors of the same shape")
        return res
