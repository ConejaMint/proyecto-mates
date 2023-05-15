# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:48:15 2023

@author: chibi
"""





###########   Librerias ###################

import pandas as pd
from math import floor
import Directorio as drc
import os


def chose_crypt(crypto):
    if crypto == 1:
        cryp = "BTC"
        by =15 #beggining year
        ey =22 #end year
        years = list(range(15,23))
        exc = "Bitstamp"
    
    elif crypto == 2:
        cryp = "ETH"
        by =17 #beggining year
        ey =22 #end year
        years = list(range(17,23))
        exc = "Gemini"
    
    elif crypto == 3:
        cryp = "XRP"
        by =17 #beggining year
        ey =22 #end year
        years =list(range(17,23))
        exc = "Bitstamp"
        
    elif crypto == 4:
        cryp = "USDC"
        by =22 #beggining year
        ey =22 #end year
        exc = "Bitstamp"
       
    elif crypto == 5:
        cryp = "USDT"
        by =22 #beggining year
        ey =22 #end year
        exc = "Bitstamp"
        
    
    elif crypto == 6:
        cryp = "DOGE"
        by =22 #beggining year
        ey =22 #end year
        exc = "Gemini"
        
    
    elif crypto == 7:
        cryp = "LTC"
        by =19 #beggining year
        ey =22 #end year
        years = list(range(19,23))
        exc = "Gemini"
        
        
        
    elif crypto == 8:
        cryp = "SHIB"
        by =22 #beggining year
        ey =22 #end year
        exc = "Gemini"
        
        
        
    elif crypto == 9:
        cryp = "BCH"
        by =18 #beggining year
        ey =22 #end year
        years = list(range(18,23))
        exc = "Bitstamp"
    
    elif crypto == 10:
        cryp = "XMR" # En USDT
        by =20 #beggining year
        ey =22 #end year
        exc = "Binance"
        
    elif crypto == 11:
        cryp = "ZEC"
        by =21 #beggining year
        ey =22 #end year
        years = [18,19,21,22]
        exc = "Gemini"
        
    return [cryp,by,ey,years,exc]



cripto = [chose_crypt(1)]#,chose_crypt(3),chose_crypt(7), chose_crypt(9),chose_crypt(11)]

for moneda in cripto:
    cryp  = moneda[0]
    by    = moneda[1]
    ey    = moneda[2]
    years =  moneda[3]
    ex    = moneda[4]
    
    print(cryp)

    ########## Path ####################
    
    
    U = drc.raiz
    #Bd = "Ensemble/"
    Bd = f"BasesDatos/{cryp}_CompData/"
    Bds = f"BasesDatos/{cryp}_TrimV10_CompData/"
    
    mainpath = os.path.join(U,Bd)
    file = f"{cryp}_LogDeltas{by}-{ey}.txt"
    savingpath = os.path.join(U,Bds)
    
    C = pd.read_csv(mainpath + file, sep = " ")
    l = C["logs"]
    f = C["fechas"]
    
    
    # ----------------------------------------------------------
    # 1440 numero de minutos por la diferencia de los logaritmos 
    # total 1438 por que excel empieza en 2
    # mi 1440 es el 1438 de excel
    
    minutos = len(C)
    n_trim = floor((len(l)-132481)/14400)+2
   
    
    counter = 0
    for i in range(0,n_trim):
        if i == 0:
           trim =  l[0:92*(1440)-1]
           trim_date = f[0:92*(1440)-1]
           
           
        else:
           trim = l[(i*10*1440)-1:1440*(92+i*10)-1]
           trim_date = f[(i*10*1440)-1:1440*(92+i*10)-1]
        
        counter += 1
        dic_trim = {"fecha":trim_date,
                    f"trim {counter}":trim
                    }
        df = pd.DataFrame(dic_trim)
        df.to_csv(savingpath + f"TrimNF_{counter}.csv", index = False)
        #Trim_NF (nueva fecha) corrige el error de formato de fecha 
        
    print(n_trim)
        