
import os
import sqlite3
from bottle import route,run,TEMPLATE_PATH, jinja2_view, static_file, request,redirect

from modelo_datos import BASE_DATOS

TEMPLATE_PATH.append(os.path.join(os.path.dirname(__file__), 'templates'))

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

@route('/')
@jinja2_view('home.html')
def hola():
    cnx= sqlite3.connect(BASE_DATOS)
    consulta = 'SELECT id, nombre, subnombre, raza, elemento, cc, ataque, defensa, vida, equip_1, equip_2, festival, habilidad_1, habilidad_2, ultimate, caracteristicas, gracia, reliquia from personajes'
    cursor=cnx.execute(consulta)
    filas = cursor.fetchall()
    cnx.close()

    return{'datos': filas}

@route('/editar')
@route('/editar/<id:int>')
@jinja2_view('formulario.html')
def mi_form(id=None):
    # cnx=sqlite3.connect(BASE_DATOS)
    # consulta = "select * from t_ocupacion"
    # cursor= cnx.execute(consulta)
    # ocupaciones = cursor.fetchall()
    
    if id is None:
        return {}
    else:
        cnx=sqlite3.connect(BASE_DATOS)
        consulta=f'SELECT id, nombre, subnombre, raza, elemento, cc, ataque, defensa, vida, equip_1, equip_2, festival, habilidad_1, habilidad_2, ultimate, caracteristicas, gracia, reliquia from personajes where id="{id}"'
        cursor= cnx.execute(consulta)
        filas = cursor.fetchone()
        
        
    cnx.close()
    return {'datos': filas}

@route('/eliminar/<id:int>')
def eliminar(id):
        cnx= sqlite3.connect(BASE_DATOS)
        consulta = f'delete from personajes where id ="{id}"'
        cnx.execute(consulta)
        cnx.commit()
        cnx.close()
        redirect('/')


@route('/guardar', method='POST')
def guardar():
    id = request.POST.id
    nombre = request.POST.nombre
    subnombre = request.POST.subnombre
    raza= request.POST.raza
    elemento = request.POST.elemento
    cc = request.POST.cc
    ataque = request.POST.ataque
    defensa = request.POST.defensa
    vida = request.POST.vida
    equip_1 = request.POST.equip_1
    equip_2 = request.POST.equip_2
    festival = request.POST.festival
    habilidad_1 = request.POST.habilidad_1
    habilidad_2 = request.POST.habilidad_2
    ultimate = request.POST.ultimate
    caracteristicas= request.POST.caracteristicas
    gracia = request.POST.gracia
    reliquia = request.POST.reliquia

    cnx=sqlite3.connect(BASE_DATOS)
    if id =='':#alta
        consulta='insert into personajes( nombre, subnombre, raza, elemento, cc, ataque, defensa, vida, equip_1, equip_2, festival, habilidad_1, habilidad_2, ultimate, caracteristicas, gracia, reliquia) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        cnx.execute(consulta,(nombre, subnombre, raza, elemento, cc, ataque, defensa, vida, equip_1, equip_2, festival, habilidad_1, habilidad_2, ultimate, caracteristicas, gracia, reliquia))
    else:#Actualizacion
        consulta = 'update personajes set nombre=?, subnombre=?, raza=?, elemento=?, cc=?, ataque=?, defensa=?, vida=?, equip_1=?, equip_2=?, festival=?, habilidad_1=?, habilidad_2=?, ultimate=?, caracteristicas=?, gracia=?, reliquia=? where id =?' 
        cnx.execute(consulta,(nombre, subnombre, raza, elemento, cc, ataque, defensa, vida, equip_1, equip_2, festival, habilidad_1, habilidad_2, ultimate, caracteristicas, gracia, reliquia,id))
        
    cnx.commit()
    cnx.close()
    redirect('/')









run(host='localhost',port=8080, debug=True)