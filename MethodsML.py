#import gspread
import requests as rq
#import json
import time
#import smtplib as mail



def get_date():
    f = '%Y-%m-%d'
    now = time.localtime()
    return time.strftime(f, now)



def search_ml(search, num_paginas, precio_min, precio_max):
    busqueda=search.replace(" ", "%20")
    l=[]
    precio_min_link=precio_min
    precio_max_link=precio_max
    url="https://api.mercadolibre.com/sites/MLA/search?q={}&limit=50&price={}-{}&ITEM_CONDITION=2230581&offset=".format(busqueda, precio_min_link, precio_max_link)
    for b in range(num_paginas):
        r=rq.get(url+str(b*50)).json()
        for a in r["results"]:
            l.append(a)
    return l
    
