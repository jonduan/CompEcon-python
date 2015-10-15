"""
DEMSLV03 Compute fixedpoint of f(x) = x^0.5

Compute fixedpoint of f(x) = x^0.5 using Newton, Broyden, and function iteration methods.
Initial values generated randomly. Some alrorithms may fail to converge, depending on the initial value.
True fixedpoint is x=1.
"""

import numpy as np
from numpy.linalg import norm
from compecon import NLP
from compecon.tools import tic, toc

''' Randomly generate starting point '''
xinit = np.random.rand(1) + 0.5

''' Set up the problem '''
def g(x):
    return np.sqrt(x)

problem_as_fixpoint = NLP(g, xinit)

''' Equivalent Rootfinding Formulation '''
def f(x):
    fval = x - np.sqrt(x)
    fjac = 1-0.5 / np.sqrt(x)
    return fval, fjac

problem_as_zero = NLP(f, xinit)

''' Compute fixed-point using Newton method '''
t0 = tic()
x1 = problem_as_zero.newton()
t1 = 100 * toc(t0)
n1 = problem_as_zero.fnorm

''' Compute fixed-point using Broyden method '''
t0 = tic()
x2 = problem_as_zero.broyden()
t2 = 100 * toc(t0)
n2 = problem_as_zero.fnorm

''' Compute fixed-point using function iteration '''
t0 = tic()
x3 = problem_as_fixpoint.fixpoint()
t3 = 100 * toc(t0)
n3 = norm(problem_as_fixpoint.fx - x3)

''' Print table header '''
print('Hundredths of seconds required to compute fixed-point of g(x)=sqrt(x)')
print('using Newton, Broyden, and function iteration methods, starting at')
print('x = {:4.2f}\n\n'.format(*xinit))
print('Method       Time   Norm of f         x\n', '-' * 40)
print('Newton   {:8.2f}    {:8.0e}     {:5.2f}'.format(t1, n1, *x1))
print('Broyden  {:8.2f}    {:8.0e}     {:5.2f}'.format(t2, n2, *x2))
print('Function {:8.2f}    {:8.0e}     {:5.2f}'.format(t3, n3, *x3))