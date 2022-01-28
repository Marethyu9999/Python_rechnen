import asyncio

async def input():
    # input of variables a,b,c
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    return a, b, c

async def tags(a):
    # adding tags to the variables based on the formulas: a>0, 0<a<1, a<0
    dir = {}
    if a > 0:
        dir["gestreckt"] = True
    elif a < 0 < 1:
        dir["gestaucht"] = True
    if a < 0:
        dir["negativ"] = True
    return dir


