import discord
from discord.ext import commands
from random import randint

num_ant = [4, 26, 2, 3, 1]

def random_num(a: int, b: int):
    global num_ant

    disponibles = [n for n in range(a, b + 1) if n not in num_ant]

    if not disponibles:
        num_ant.clear()

    c = randint(a, b)

    while c in num_ant:
        c = randint(a, b)

    num_ant.append(c)
    num_ant.pop(0)

    return c




muletillas = ["mi rey", "nigga", "joder macho", "estoy hasta la polla", "germa", "por cierto que tal noi?", "bro", "osea me ceba una barbaridad", "fr", 
              "allahu hakbar", "extraño a nesi", "men stfu"]

emociones = ["concentrado", "brotado", "en un one v", "fumando un porro", "haciendo un joint", "escuchando babylon", "rayado", 
             "ocupado haciendome fotos para ligar", "desbrozando"]

active_messages = ["te juro que te voy a matar", "suicidate bro que te gano en un one v",
                     "que pasa que tu padre te amamantaba cuando eras bebe?", "bro como se nota que no tienes figura paterna", 
                     "bro que te calles que estoy killeando un boss del dark souls", "bro has visto este juego?", "nigga stfu y mira esto", "cabron callate un puto mes",
                     "hay gente que no se ha jugado un persona en la vida y se nota pila 4r", "buah es que como quiero pegar a un facha ahora mismo",
                     "te has esucuchado este tema?", "es que a mi me flipan los personas", "como me encantan los dark souls joder", "soy dante de dmc y no hay discusion",
                     "soy shadow y quien diga lo contrario esta en lo incorrecto", "pero 4r que no sabias eso? yo pensaba que era sentido comun", 
                     f"Estoy {emociones[random_num(0,len(emociones)-1)]}, no hables, {muletillas[random_num(0,len(muletillas)-1)]}"]

async def gestionar_mencion(message, bot):
    await message.channel.send(active_messages[random_num(0,len(active_messages)-1)])
