#!/usr/bin/env python3

# Opcodes
""""
         1 2    3
i.- adds a b -> c

"""

l = open('lvl2_input.txt').readlines()
l = l[0].strip('\n').split(',')

for i in range(len(l)):
    l[i] = int(l[i])

#f = [int(i.strip('\n')) for i in open('input.txt').readlines()]
#f = [i.strip('\n').split(',') for i in open('lvl1_input.txt').readlines()]
print(l)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

