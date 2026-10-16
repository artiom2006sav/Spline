import sympy as sp
import pandas as pd
import numpy as np



def h_array(x_values):
    h_array = []
    for i in range(len(x_values) - 1):
        h_i = x_values[i+1] - x_values[i]
        h_array.append(h_i)

    return h_array

def SplineFormule(h):
    spline_formule = {'a_i' : 1, 'b_i' : h,  'c_i' : h**2, 'd_i' : h**3}
    return spline_formule

def SplineDeriv(h):
    spline_deriv = {'a_i' : 0, 'b_i' : 1, 'c_i' : 2*h, 'd_i' : 3*h**2}
    return spline_deriv

def SplineSecondDeriv(h):
    spline_second_deriv = {'a_i' : 0, 'b_i' : 0, 'c_i' : 2, 'd_i' : 6*h}
    return spline_second_deriv

def SLU(y_values, h_array):
    n = len(h_array) 
    for i in range(n):
        h = h_array[i]
        first = {'a_i' : 1, 'b_i' : 0, 'c_i' : 0, 'd_i' : 0}
        second = SplineFormule(h)

        if i < n - 1:
            third = {
                'current_deriv': SplineDeriv(h), 
                'next_deriv_b': -1        
            }
            fourth = {
                'current_second_deriv': SplineSecondDeriv(h), 
                'next_second_deriv_c': -2                
            }








