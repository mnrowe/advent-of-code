#!/usr/bin/env python3

def calc_fuel_from_mass(f):
    """
    Basic calculation for fuel and mass.
    >>> calc_fuel_from_mass(14)
    2
    >>> calc_fuel_from_mass(1969)
    654
    >>> calc_fuel_from_mass(12)
    2
    >>> calc_fuel_from_mass(100756)
    33583
    """

    return int((f/3))-2

def fuel_from_fuel(m):
    """
    Turn fuel into more fuel.
    >>> fuel_from_fuel(14)
    2
    >>> fuel_from_fuel(1969)
    966
    """
    tm = 0 
    while m > 0:
        m = calc_fuel_from_mass(m)
        if m < 0:
            m = 0

        tm += m
    return tm 

f = [int(i.strip('\n')) for i in open('input.txt').readlines()]

mls = [calc_fuel_from_mass(i) for i in f]
mes = [fuel_from_fuel(m) for m in mls]

print(sum(mls) + sum(mes))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

