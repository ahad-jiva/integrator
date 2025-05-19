import math

# some example functions you can use
# string them together to create any elementary function
# make sure to pass x as a float

def main_f(x):
    # use the functions below to construct an elementary function that will be passed to main
    return exp(-0.5 * poly(x, 2))

def poly(x, p):
    return pow(x, p)

def exp(x): # e^(x)
    return math.exp(x)

def sin(x):
    return math.sin(x)

def sinh(x):
    return math.sinh(x)

def arcsin(x):
    return math.asin(x)

def arcsinh(x):
    return math.asinh(x)

def cos(x):
    return math.cos(x)

def cosh(x):
    return math.cosh(x)

def arccos(x):
    return math.acos(x)

def arccosh(x):
    return math.acosh(x)

def tan(x):
    return math.tan(x)

def tanh(x):
    return math.tanh(x)

def arctan(x):
    return math.atan(x)

def arctah(x):
    return math.atanh(x)

def log(x, base):
    return math.log(x, base)
