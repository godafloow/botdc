import discord
from random import randint
from discord.ext import commands
from config_dinamica import obtener_id_purgatorio


none_canal = ["Joder macho mira que eres putamente anormal, esa mierda no existe", "Nigga, donde esta eso?", 
              "Macho joder, es que para que coño me dices nada si no existe si quiera",
              "Bro, eres autista? la mierda esa no existe",
              "Nigga que eso no existe, osea encima tengo que crearlo yo y hacerte de padre o que?"]



none_miembro = ["Si bro y a quien muevo? es sentido comun tener que poner a alguien",
                "nigga, a quien coño quieres que mueva si no has mencionado a nadie?",
                "stfu men, menciona a alguien y luego hablamos",
                "tengo que hacerte de padre y adivinar a quien mover o que?",
                "puto anormal que no me has dicho a nadie",
                "bro osea no mencionas a nadie? para esto he parado de jugar al dark souls 3? si quieres te cuento el lore eh"]


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
        



class Purgatorio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="purgatorio")
    @commands.guild_only()
    
    
    async def purgatorio(
        self,
        ctx,
        miembro: discord.Member = None
    ):

        if miembro is None:
                await ctx.send(none_miembro[random_num(0,len(none_miembro)-1)])
                return

        none_miembrocanal = ["Nigga, eres autista? No esta en voz, osea es sentido comun", f"El gilipollas del {miembro} no esta ahi bro",
                        "Nigga joder me han matado por tu puta culpa, joder encima el puto subnormal no esta, osea eres retrasado o que?",
                        "Bro, que no esta, que por alguna puta razon no esta", "Germa, callate la puta boca porque el cabron ni si quiera esta ahi",
                        "Joder, encima tengo que venir y hacerte de padre para que el sunormal no este si quiera en voz"]

        move_success = [f"{miembro.mention} te he enviado un rato para que cierres la puta boca, que solo yo puedo hablar",
                        f"{miembro.mention}, mira, o cierras el puto hocico o te echo de mi server 4r", f"{miembro.mention} te callas la puta boca de una vez?",
                        f"{miembro.mention} nigga estoy contando una mierda y me interrumpes o sea callate", 
                        f"{miembro.mention} callate la boca que no me dejas jugar el final del persona",
                        f"{miembro.mention} nigga shut up estoy viendo un video de joseju 4r", 
                        f"{miembro.mention} la proxima vez en vez de esto te pongo la boca en un bordillo como si fuera nazi"]

        ID_CANAL = obtener_id_purgatorio()
        canal = ctx.guild.get_channel(ID_CANAL)


        if canal is None:
            await ctx.send(none_canal[random_num(0, len(none_canal)-1)])
            return

        if miembro.voice is None:
            await ctx.send(none_miembrocanal[random_num(0, len(none_miembrocanal)-1)])
            return

        try:
            await miembro.move_to(canal)
            await ctx.send(move_success[random_num(0,len(move_success)-1)])
        except discord.Forbidden:
            await ctx.send("Nigga, no me deja mover a esa persona, no tengo los permisos")
        except discord.HTTPException as error:
            await ctx.send(f"Mira te explico el lore, por alguna razon los inutiles del discord han hecho x cosa y por lo que sea, no va bien la mierda esta")
        except discord.ext.commands.errors.MissingRequiredArgument:
            await ctx.send()

async def setup(bot):
    await bot.add_cog(Purgatorio(bot))
