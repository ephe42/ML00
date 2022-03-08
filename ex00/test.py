#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

from matrix import Vector

if __name__ == "__main__":
    print("__init__")
    print(Vector([1.0, 2e-3, 3.14, 5.0]).values)
    print(Vector(4).values)
    # Vector(-1)
    print(Vector((10, 12)).values)
    # print(Vector((3, 1)).values)
    # v = Vector((1, 1))
    # print(v.values)
    # Vector((4, 7.1))

    print("\n__mul__ and __rmul__")
    v = Vector(4)
    print(v.values)
    print(v * 4)
    print(4.0 * v)
    # v * "hi"
    # print((v * v).values)

    print("\n__add__, __radd__, __sub__ and __rsub__")
    v = Vector(4)
    v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
    print((v + v2).values)
    # v + Vector([0.0, 0.0, 0.0, 0.0])
    # v + "hello"
    # v + None
    # v + 2
    # 2 + v
    print((v - v2).values)
    # v - Vector([0.0, 0.0, 0.0, 0.0])
    # v - "hello"
    # v - None
    # v - 2
    # 2 - v

    print("\n__div__ and __rdiv__")
    print(Vector(4) / 2)
    print(Vector(4) / 3.14)
    # Vector(4) / 0
    # Vector(4) / None
    # None / Vector(4)
    # 3 / Vector(3)
