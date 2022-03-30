import sqlite3
import os


BASE_DATOS=os.path.join(os.path.dirname(__file__),'personajes.db')


creacion="""
        create table personajes(
            id integer primary key autoincrement,
            nombre text,
            subnombre text,
            raza text,
            elemento text,
            cc text,
            ataque text,
            defensa text,
            vida text,
            equip_1 text,
            equip_2 text,
            festival text,
            habilidad_1 text,
            habilidad_2 text,
            ultimate text,
            caracteristicas text,
            gracia text,
            reliquia text)
"""

def crear_bd():
    cnx= sqlite3.connect(BASE_DATOS)
    cnx.execute(creacion)
    cnx.close()


