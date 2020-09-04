#!/usr/bin/python
# encoding: utf-8
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EncuentraLibre.settings.production')
django.setup()

from apiforms.models import Busqueda, Resultado, Usuario
from MethodsML import *
from email.mime.text import MIMEText
from email.header import Header
import smtplib


num_paginas=20
usuarios_id=list(Usuario.objects.values('id'))



for usuario_id in usuarios_id:
    
    Buscar=list(Busqueda.objects.values().filter(usuario_id=usuario_id['id']))
   

    
    results=[]
    for i in range(len(Buscar)):
        idss=list(Resultado.objects.values('ids').filter(usuario_id=usuario_id['id']))

        ids=[d['ids'] for d in idss]
        
        
        precio_min=float(Buscar[i]['precio_min'])
        precio_max=float(Buscar[i]['precio_max'])

        search_raw=search_ml(Buscar[i]['busqueda'], num_paginas, precio_min, precio_max)   

        busqueda_id=Busqueda.objects.get(busqueda=Buscar[i]['busqueda'])
        usuario_instance=Usuario.objects.get(id=usuario_id['id'])
        usuario_email=Usuario.objects.values('email').filter(id=usuario_id['id'])
        
        publicaciones=[]

        for publication in search_raw:
            publicaciones.append(publication)
                    
        publicaciones_mostrar=[]
        for b in range(len(publicaciones)):  
            if publicaciones[b]["id"] not in ids:        
                id_producto=publicaciones[b]["id"]
                titulo=publicaciones[b]["title"]
                precio=publicaciones[b]["price"]
                link=publicaciones[b]["permalink"]
                
                publicaciones_mostrar.append(link)

                Articulos_agregar= Resultado(busqueda=busqueda_id, ids=id_producto, titulo=titulo, precio=precio, link=link, usuario=usuario_instance)
                Articulos_agregar.save()
                
        if len(publicaciones_mostrar)<=10 and len(publicaciones_mostrar)>0:
            server = smtplib.SMTP("smtp.encuentralibre.com.ar", 587)#port
            server.ehlo()
            server.starttls()
            server.login('aviso@encuentralibre.com.ar', 'yokapo123')
            body = 'Se encontro una/unas publicación/nes: '+'\n' .join(publicaciones_mostrar)
            msg = MIMEText(body,'plain','utf-8')
            subject = 'Publicacion/es encontrada'
            msg["Subject"] = Header(subject, 'utf-8')
            From = 'aviso@encuentralibre.com.ar'
            to = usuario_email[0]['email']
            msg["From"] = Header(From, 'utf-8')
            msg["To"] = Header(to, 'utf-8')
            txt = msg.as_string()
            server.sendmail(From, to, txt)
            
        """user= 'encuentralibree@gmail.com'
        password = 'yokapo123'
        Remitente='encuentralibree@gmail.com'
        destinitario= usuario_email[0]['email']
        asunto= 'Publicacion/es encontrada'
        mensaje='Se encontro una/unas publicación/nes: '+'\n' .join(publicaciones_mostrar)
        gmail =smtplib.SMTP ('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.ehlo()
        gmail.login(user, password)
        gmail.set_debuglevel(1)
        header =MIMEMultipart()
        header['subject']=asunto
        header['From']=Remitente
        header['To']=destinitario
        mensaje= MIMEText (mensaje, 'plain')
        header.attach(mensaje)
        gmail.sendmail(Remitente, destinitario, header.as_string())
        gmail.quit()"""
        

print("trabajo realizado")