def square(x):
    return x*x

def map(f, lst):
    return [f(elt) for elt in lst]

y = map(square, [1,2,3,4,5,6])

