import pandas as pd # pandas k nacitani dat z excelu
import numpy as np # numpy pro vypocty
import math
from typing import Iterable, Any


def saturovatelny_absorber(intenzita:Iterable[float], transmitance:Iterable[float])->dict[str, Any]:
    vlastnosti = pd.DataFrame(zip(intenzita, transmitance), columns=("intenzita", "transmitance"))
    nesaturovatelne_ztraty = 100 - max(vlastnosti["transmitance"])
    hloubka_modulace = (max(vlastnosti["transmitance"]) + min(vlastnosti["transmitance"]))/2
    saturacni_intenzita = vlastnosti[vlastnosti["transmitance"].between(hloubka_modulace-10, hloubka_modulace+10)] # tohle je hodně známka punku

    return {"nesaturovatelne_ztraty":nesaturovatelne_ztraty,
            "hloubka_modulace":hloubka_modulace,
              "saturacni_intenzita":np.mean(saturacni_intenzita["intenzita"])}

