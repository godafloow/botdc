import discord
from discord.ext import commands
from random import randint

num_ant = [4, 26, 2, 3, 1]


class active(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    active_messages=["te juro que te voy a matar", "suicidate bro que te gano en un one v",
                     "que pasa que tus padre te amamantaba cuando eras bebe?", "bro como se nota que no tienes figura paterna", 
                     "bro que te calles que estoy killeando un boss del dark souls", "bro has visto este juego?", "nigga stfu y mira esto", "cabron callate un puto mes",
                     "hay gente que no se ha jugado un persona en la vida y se nota pila 4r", "buah es que como quiero pegar a un facha ahora mismo",
                     "te has esucuchado este tema?", "es que a mi me flipan los personas", "como me encantan los dark souls joder", "soy dante de dmc y no hay discusion",
                     "soy shadow y quien diga lo contrario esta en lo incorrecto", "pero 4r que no sabias eso? yo pensaba que era sentido comun", 
                    ]



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

    @commands.command(name="active")
    @commands.guild_only()
    async def mi_comando(self, ctx):
        # Aquí va el código de tu función
        await ctx.send()


async def setup(bot):
    await bot.add_cog(active(bot))