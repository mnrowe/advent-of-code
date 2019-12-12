#!/usr/bin/env python3

mass_list = [
114106,
87170,
133060,
70662,
134140,
125874,
50081,
133117,
100409,
95098,
70251,
134043,
87501,
85034,
110678,
80615,
64647,
88555,
106387,
143755,
101246,
142348,
92684,
62051,
94894,
65873,
78473,
64042,
147982,
145898,
85591,
121413,
132163,
94351,
80080,
73554,
106598,
135174,
147951,
132517,
50925,
115752,
114022,
73448,
50451,
56205,
81474,
90028,
124879,
137452,
91036,
87221,
126590,
130592,
91503,
148689,
86526,
105924,
52411,
146708,
149280,
52100,
80024,
115412,
91204,
132726,
59837,
129863,
140980,
109574,
103013,
84105,
138883,
144861,
126708,
140290,
54417,
138154,
125187,
91537,
90338,
61150,
61702,
95888,
100484,
82115,
122141,
63986,
138234,
54150,
57651,
124570,
88460,
112144,
112334,
119114,
58220,
143221,
86568,
148706,
]

fuel_list = []
fuel_sum = 0

def divide_by_three_round_sub(i):
    """
    Basic calculation for fuel and mass.
    >>> divide_by_three_round_sub(14)
    2
    >>> divide_by_three_round_sub(1969)
    654
    """

    return int((i/3))-2

def calc_fuel(m):
    """ 
    Calculate fuel list based on mass list
    >>> calc_fuel(14)
    2
    >>> calc_fuel(1969)
    654
    """

    return divide_by_three_round_sub(m)


for i, m in enumerate(mass_list):
    fuel_list.append(calc_fuel(m))

fuel_sum = sum(fuel_list)

while fuel_sum > 0:
    fuel_sum = calc_fuel(fuel_sum)
    print(fuel_sum)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
