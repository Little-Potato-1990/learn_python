'''
Description:  
Author: ren qian
Date: 2022-01-11 18:55:10
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# s = (x * x for x in range(5))
# for ss in s:
#   print(ss)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

# f = fib(10)
# for x in f:
#     print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

