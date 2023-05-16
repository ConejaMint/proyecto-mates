# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:45:26 2023

@author: Jessica
"""


import pandas as pd
import Directorio as drc
import numpy as np
from criptos import chose_crypt

cripto = [chose_crypt(11)]#,chose_crypt(3),chose_crypt(7), chose_crypt(9),chose_crypt(11)]

for moneda in cripto:
    cryp  = moneda[0]
    by    = moneda[1]
    ey    = moneda[2]
    years =  moneda[3]
    ex    = moneda[4]
    
    for y in range(by,ey+1): 

        data_real = pd.read_csv(drc.base_data +
f"{cryp}_LogsDeltas/LogsDeltas20{y}.csv")
        lr = data_real["logs"]
        print(cryp,f"20{y}")
        print("mu-logs: ",np.mean(lr))
        print("d.est: ",np.std(lr))
        print("===============================")

