from decimal import Decimal
import numpy as np


def remove(n): # pomocna funkce pro round_to_reference co uz uprimne nevim co dela
    if Decimal(n) == Decimal(n).to_integral():
        return int(n) 
    else: return n

def zaokrouhleni(zaokrouhlovana_hodnota:float, pocet_cifer:int | None = None, 
                 reference:float | None = None)->float | tuple[float, float]:
    """Zaokrouhleni vstupni hodnoty bud na pozadovany pocet cifer, nebo dle první platne cifry reference

    Args:
        zaokrouhlovana_hodnota (float): Hodnota k zaokrouhleni.
        pocet_cifer (int, optional): Explicitne zadany pocet cifer na ktere se zaokrouhluje.
        reference (float, optional): Reference podle ktere se zaokrouhluje.

    Returns:
        float|tuple[float, float]: Hodnota zaokrouhlena na pozadovany pocet desetinnych mist, 
            pripadne dvojice (hodnota, reference), obe zaokrouhlene na prvni platnou cifru reference.
    """

    if pocet_cifer != None:
        return remove(round(zaokrouhlovana_hodnota, pocet_cifer))
    else:
        pocet_cifer = -int(np.floor(np.log10(reference)))
        return remove(round(zaokrouhlovana_hodnota, pocet_cifer)), \
            remove(round(reference, pocet_cifer))