from scipy import misc 

def f(x): 
    return x**3

def dx(f, x):
    return abs(0-f(x))

def derivative(f,x):
    return misc.derivative(f, x, dx=1e-6)

def newtons_method(f,xi,e):
    delta = dx(f,xi) 
    if(delta < e):
        return xi 
    else:
        df = derivative(f,xi)
        xi = xi - (f(xi)/df)
        delta = dx(f,xi)
        return newtons_method(f,xi,e)

def f(x):
    return 6*x**5-5*x**4-4*x**3+3*x**2

if __name__ == "__main__":
   x0s = [0,0.5,1]
   for x in x0s:
       print("Root: ", round(newtons_method(f,x,1e-5),4))
