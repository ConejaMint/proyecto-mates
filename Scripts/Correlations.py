# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:18:29 2023

@author: chibi
"""

"""
Código para tabla de correlación entre Dkl e I
"""

import Directorio as drc
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np
from criptos import chose_crypt 

type_data = input("data: d or surrgate: s ")

cripts = []
corp = []
cork = []
cors = []

cripto = [chose_crypt(1),chose_crypt(2), chose_crypt(3),chose_crypt(7), chose_crypt(9)]

for moneda in cripto:
    cryp  = moneda[0]
    by    = moneda[1]
    ey    = moneda[2]
    years =  moneda[3]
    ex    = moneda[4]
    
    if type_data == "d":
        dkl = pd.read_csv(drc.raiz + drc.adc_trnds + f"{cryp}/ResultadosKullBackLeibler/DKL_{cryp}_TV10.csv" )["DKL"]
        efb = pd.read_csv(drc.raiz + drc.adc_e + f"{cryp}/IL3_trim_{cryp}.csv")["I"]
        file_name = "Crypt_corr.csv"
        
        
    elif type_data == "s": 
        dkl = pd.read_csv(drc.raiz + drc.adc_trnds + f"{cryp}/ResultadosKullBackLeibler_Shuffled/DKL-shuf_{cryp}_TV10.csv" )["DKL"]
        efb = pd.read_csv(drc.raiz + drc.adc_e + f"{cryp}/IsL3_trim_{cryp}.csv")["I"]
        file_name = "Crypt_corr_surr.csv"
    
    
    corr_p =  dkl.corr(efb, method = "pearson") 
    corr_k =  dkl.corr(efb, method = "kendall")
    corr_s =  dkl.corr(efb, method = "spearman")
    
    print(cryp, corr_p, corr_k, corr_s)
    cripts.append(cryp)
    corp.append(corr_p)
    cork.append(corr_k)
    cors.append(corr_s)
    
    
dict_cript = {"Crypto": cripts,
             "Pearson": corp,
             "Kendall": cork,
             "Spearman": cors
             }

df = pd.DataFrame(dict_cript, columns = ["Crypto","Pearson","Kendall", "Spearman"])
print(50*"=")
print(df)
df.to_csv(drc.raiz + drc.adc + file_name, index = False)
   
    #x_axis = np.arange(len(dkl))

    #plt .plot(x_axis,dkl)
    #plt.plot(x_axis,efb)



