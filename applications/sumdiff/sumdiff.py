"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
add_dict = {}
sub_dict = {}

for i in q:
    for j in q:
        add_dict[f"f({i}) + f({j})"] = (f(i) + f(j), f(i), f(j))
        sub_dict[f"f({i}) - f({j})"] = (f(i) - f(j), f(i), f(j))

for i in add_dict.items():
    for j in sub_dict.items():
        if i[1][0] == j[1][0]:
            print(f"{i[0]} + {j[0]}    {i[1][1]} + {i[1][2]} = {j[1][1]} - {j[1][2]}")



