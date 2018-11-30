'''
Please read the README.md for guide and limitations of this program.
Author: Howard Lin and Danny Lu
'''
from scipy import misc 
from math import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
import time

'''
    Calculates Delta of the function, which is the error
    f: function that takes in an x
    x: value
'''
def dx(f, x):
    return abs(0-f(x))

'''
    Calculates the dertivate of the function at x
    f: function that takes in an x
    x: value

    NOTE: Currently this is using a library that approximates the derivative,
    and is thus accurate to 12 decimal places at the moment.
'''
def derivative(f,x):
    return misc.derivative(f, x, dx=1e-12)

'''
    Newton's Method 
    f: function that takes in an x
    xi: value (x0 when initially called)
    e: Maximum error (best if under 11 decimal places)
'''
def newtons_method(f,xi,e):
    tangents = []
    delta = dx(f,xi) 
    while(delta > e):
        df = derivative(f,xi)
        xi = xi - (f(xi)/df)
        delta = dx(f,xi)
        def t(x):
            return df * (x - xi) + f(x)
        tangents.append(t)
    return (xi, tangents)

'''
    Will ask user for a function and then return said function as well as string representation
'''
def function_parser():
    safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e','exp','fabs', 'floor', 'fmod','frexp','hypot','ldexp', 'log', 'log10','modf', 'pi','pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan','tanh']
    safe_dict = dict([(k,locals().get(k,None)) for k in safe_list]) 
    expr = input("Input function please: ")
    def f(x):
        safe_dict['x'] = x
        return eval(expr, {"__builtins__":None},safe_dict)
    return (f, expr)

if __name__ == "__main__":
    (f, expr) = function_parser()
    xi = int(input("Input initial point please: "))
    e = 1e-11
    (root, tangents) = newtons_method(f,xi,e)
    root = round(root, 4)
    print("Root: ", root)
    x = np.arange(-10, 10, 0.01)
    plt.plot(x, f(x))
    delta = dx(f,xi) 
    while(delta > e):
        df = derivative(f,xi)
        if(df == 0):
            plt.annotate('You selected an initial value that results in a division by zero', 
                xy=(0, 0),  
                xycoords='data',
                textcoords='offset points',
                xytext=(-130, 30),
                arrowprops=dict(arrowstyle="->"))
            plt.annotate('Please restart program and select different initial point.', 
                xy=(0, 0),  
                xycoords='data',
                textcoords='offset points',
                xytext=(-130, -30),
                arrowprops=dict(arrowstyle="->"))
            break
        xi = xi - (f(xi)/df)
        delta = dx(f,xi)
        plt.plot(x,(df * (x - xi)) + f(xi),linestyle='dashed')
    plt.axis([-10, 10, -10, 10])
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.title('Newtons Method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(['f(x) = '+ expr])
    plt.annotate('Root approx. at ' + str(root), 
             xy=(root, 0),  
             xycoords='data',
             textcoords='offset points',
             xytext=(0, -50),
             arrowprops=dict(arrowstyle="->"))
    plt.show()

