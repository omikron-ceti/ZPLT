import numpy as np
from typing import Iterable

def normalize(data:Iterable)->Iterable:
    minimum = np.min(data)
    maximum = np.max(data)
    normalized_data = (data-minimum)/(maximum-minimum)
    return normalized_data

def exponenciala(x, a, b, c):
    return a*np.exp(b*x)+c

def linear_fit(x, a, b): 
    """Lineárni funkce y = a*x + b
    Args:
        x (int / float): bod vycislovani (namerena hodnota)
        a (int / float): koeficient
        b (int / float): konstanta
    Returns:
        float: hodnota linearni funkce s predpisem y = a*x + b v bode x
    """
    return a*x + b