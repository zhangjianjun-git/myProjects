import operator


def myFunction(a, b):
    return operator.add(a, b)

def concat(a, b):
    return operator.concat(a, b)

def contains(a, b):
    return operator.contains(a, b)

def truediv(a, b):
    return operator.truediv(a, b)

print(operator.truth(-1))
