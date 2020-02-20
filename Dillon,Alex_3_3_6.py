import random
c = (3, 4, 5)
some_values = ('a', 'b', 3)
d = 10
tup = (9, c, 11)

values = ['a', 'b', 3]

e = 6

def roll_two_dice():
    a = random.randint(1, 6)
    b = random.randint(1,6)
    print(a + b)

def guess_letter():
    let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
    print(random.choice(let))