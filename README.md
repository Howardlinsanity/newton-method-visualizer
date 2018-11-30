# Newton's Method Visualizer 
Math 351 Project, in collaboration with Danny L. 

# How does it work?
Using an initial point, it will calculate the tangent line of the function at that point and find the x-intercept of the tangent line. The process then iteratively uses that x-intercept as the next value, we find the tangent line of that value in the function, repeat, etc. It's a Numerical Method, more can be found here: https://en.wikipedia.org/wiki/Newton%27s_method

# Dependencies
All that is required so far is that you have python3 installed

# Running application
Run `python3 main.py`

# Parameters and Limitations
When you run the program, it will ask for a function - the function has to be a polynomial (i.e. Log, trig functions, etc will not work), and it must be in python math format.
So, this following will work:
- `3*(x-3)**3 + 3` (power is denoted by double asterisks)
- `x**2` (this is x squared)

The following will not work:
- `sin(x)` (only polynomials can be used)
- `3(x-3)**3 + 3` (you need the * to signify multiplication)

If you put in an initial point that will result in a division by zero somewhere in the method, the program will tell you to restart the process with a new initial point.
