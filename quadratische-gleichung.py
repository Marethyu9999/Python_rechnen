import matplotlib.pyplot as plt
import numpy as np

def input_variables():
    # input of variables a,b,c
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    return a, b, c

def tags(a):
    # adding tags to the variables based on the formulas: a>0, 0<a<1, a<0
    dir = {}
    if a > 0:
        dir["gestreckt"] = True
    elif a < 0 < 1:
        dir["gestaucht"] = True
    if a < 0:
        dir["nach unten geöffnet"] = True
    return dir

def visualising(a, b, c):
    # visualising the graph
    x = np.linspace(-10, 10, 10000)
    y = a * x**2 + b * x + c
    plt.plot(x, y)
    plt.show()

def main():
    # main function
    a, b, c = input_variables()
    dir = tags(a)
    print(dir)
    visualising(a, b, c)

if __name__ == "__main__":
    main()