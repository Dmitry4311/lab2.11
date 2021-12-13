#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def function(number):
    def function_2():
        return number + 3
    return function_2()


if __name__ == '__main__':
    k = float(input("Введите число: "))
    cnt = function(k)
    print(cnt)
