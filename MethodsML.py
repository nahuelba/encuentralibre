import requests as rq
import time

def search_ml(search, precio_min, precio_max):
    busqueda=search.replace(" ", "%20")
    l=[]
    precio_min_link=precio_min
    precio_max_link=precio_max
    url="https://api.mercadolibre.com/sites/MLA/search?q={}&limit=50&price={}-{}&ITEM_CONDITION=2230581&offset=".format(busqueda, precio_min_link, precio_max_link)
    
    request_total=rq.get(url+'0').json()

    if request_total["paging"]["total"]<=50:
        num_paginas=1
    elif request_total["paging"]["total"]<=100:
        num_paginas=2
    elif request_total["paging"]["total"]<=150:
        num_paginas=3
    elif request_total["paging"]["total"]<=150:
        num_paginas=3
    elif request_total["paging"]["total"]<=200:
        num_paginas=4
    elif request_total["paging"]["total"]<=250:
        num_paginas=5
    elif request_total["paging"]["total"]<=300:
        num_paginas=6
    elif request_total["paging"]["total"]<=350:
        num_paginas=7
    elif request_total["paging"]["total"]<=400:
        num_paginas=8
    elif request_total["paging"]["total"]<=450:
        num_paginas=9
    else:
        num_paginas=10
    
    time.sleep(7)

    for b in range(num_paginas):  
        
        r=rq.get(url+str(b*50)).json()
        time.sleep(7)
            
            
        for a in r["results"]:
            l.append(a)
    return l
    
