from scipy import misc 
from math import *

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
    Newton's Method - currently made this recursive due to simplicity, may need to convert to iterative in future
    f: function that takes in an x
    xi: value (x0 when initially called)
    e: Maximum error (best if under 11 decimal places)
'''
def newtons_method(f,xi,e):
    delta = dx(f,xi) 
    if(delta < e):
        return xi 
    else:
        df = derivative(f,xi)
        xi = xi - (f(xi)/df)
        delta = dx(f,xi)
        return newtons_method(f,xi,e)

def function_parser():
    safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e','exp','fabs', 'floor', 'fmod','frexp','hypot','ldexp', 'log', 'log10','modf', 'pi','pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan','tanh']
    safe_dict = dict([(k,locals().get(k,None)) for k in safe_list]) 
    expr = input("Input function please: ")
    def f(x):
        safe_dict['x'] = x
        return eval(expr, {"__builtins__":None},safe_dict)
    return f

if __name__ == "__main__":
    func = function_parser()
    x0s = [0,0.5,1]
    for x in x0s:
        print("Root: ", round(newtons_method(func,x,1e-5),4))
