#!/usr/bin/python
# encoding: utf-8
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EncuentraLibre.settings.production')
django.setup()

from apiforms.models import Busqueda, Resultado, Usuario
from MethodsML import search_ml
from email.mime.text import MIMEText
from email.header import Header
import smtplib

usuarios_id=list(Usuario.objects.values('id'))

#for de la cantidad de usuarios totales
for usuario_id in usuarios_id:
    
    Buscar=list(Busqueda.objects.values().filter(usuario_id=usuario_id['id']))

    results=[]
    #for de la cantidad de busquedas totales
    for i in range(len(Buscar)):
       
        idss=list(Resultado.objects.values('ids').filter(usuario_id=usuario_id['id']))
        ids=[d['ids'] for d in idss]

        precio_min=float(Buscar[i]['precio_min'])
        precio_max=float(Buscar[i]['precio_max'])

        search_raw=search_ml(Buscar[i]['busqueda'], precio_min, precio_max)   

        usuario_instance=Usuario.objects.get(id=usuario_id['id'])
        busqueda_id=Busqueda.objects.filter(busqueda=Buscar[i]['busqueda']).first()
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
            try:    
                server = smtplib.SMTP("mail.encuentralibre.com.ar", 26)#port
                server.ehlo()
                server.starttls()
                server.login('aviso@encuentralibre.com.ar', '')
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
                print('Se envio mail a ' + usuario_email[0]['email'])
            except:
                print('no se pudo enviar el mail a ' + usuario_email[0]['email'])
                
                            

print("trabajo realizado")
