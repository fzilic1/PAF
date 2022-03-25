import calculus as cal
import matplotlib.pyplot as plt

def f1(x):
    return x

print(cal.intlim(f1, 0, 1, 10))
print(cal.numint(f1, 0, 1, 10))