#!/usr/bin/env python3

''' operations '''

''' empty list '''
a = []

''' add using the last position with len function '''
print("a.insert(3)")
a.insert(len(a), 3)
print(a)

''' insert '''
print("a.insert(5)")
a.insert(0, 5)
print(a)

''' append '''
print("a.append(9)")
a.append(9)
print(a)

''' remove by value'''
print('a.remove(0)')
a.remove(9)
print(a)

''' remove by position list '''
print('a[0].pop()')
a.pop(0)
print(a)

''' remove all items '''
print('del a[:]')
del a[:]
print(a)

