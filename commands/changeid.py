import json
from pathlib import Path
import discord
from discord.ext import commands

RUTA_CONFIG = Path(__file__).resolve().parent / "config_dinamica.json"


class ChangeID(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="changeid")
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def changeid(self, ctx, canal: int):
        canal_obj = ctx.guild.get_channel(canal)

        # Si no está en caché, intenta obtenerlo de Discord
        if canal_obj is None:
            try:
                canal_obj = await self.bot.fetch_channel(canal)
            except discord.NotFound:
                await ctx.send("No encuentro ese canal.")
                return
            except discord.Forbidden:
                await ctx.send("No tengo permisos para acceder a ese canal.")
                return
            except discord.HTTPException:
                await ctx.send("Error al consultar el canal en Discord.")
                return

        # Comprueba que pertenezca a este servidor
        if canal_obj.guild.id != ctx.guild.id:
            await ctx.send("Ese canal no pertenece a este servidor.")
            return

        datos = {}

        if RUTA_CONFIG.exists():
            with RUTA_CONFIG.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

        datos["ID_CANAL_PURGATORIO"] = canal_obj.id

        with RUTA_CONFIG.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)

        await ctx.send(
            f"El canal del purgatorio ahora es {canal_obj.mention}."
        )


async def setup(bot):
    await bot.add_cog(ChangeID(bot))
