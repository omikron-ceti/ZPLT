import pandas as pd # pandas k nacitani dat z excelu
import numpy as np # numpy pro vypocty
import math
from typing import Iterable

def polomer_svazku(w_0:float, z_0:float, vzdalenost_od_ohniska:Iterable[float])->np.ndarray:
    """Výpočet poloměrů Gaussovského svazku s paramerty w_0 a z_0 pro zadané vzdálenosti od ohniska

    Args:
        w_0 (float): Poloměr svazku v ohnisku 
        z_0 (float): Rayleighova vzdálenost 
        vzdalenost_od_ohniska (Iterable[float]): Seznam vzdáleností od ohniska, pro které počítám poloměry svazku

    Returns:
        np.NDArray: Poloměry Gaussovského svazku pro zadané vzdálenosti od ohniska
    """
    return np.array([w_0*math.sqrt(1+(d/z_0)**2) for d in vzdalenost_od_ohniska])

def hustota_vykonu(vzdalenost_od_ohniska:Iterable[float], stredni_vykon:float, w_0:float, z_0:float)->np.ndarray:
    """Hustota výkonu v závislosti na poloměru svazku, možno počítat přímo z naměřených výkonů, 
    případně z transmitance a kalibrační hodnoty (např. pokud bylo měřeno napětí na fotodiodě). Předpokládá se kruhový průřez svazku.

    Args:
        w_0 (float): Poloměr svazku v ohnisku 
        z_0 (float): Rayleighova vzdálenost 
        polomer (Iterable[float]): Poloměry svazku
        stredni_vykon (float): Střední výkon

    Returns:
        np.ndarray: Hustoty výkonu
    """
    polomer = polomer_svazku(w_0, z_0, vzdalenost_od_ohniska)
    return stredni_vykon/(2*math.pi*polomer**2)
