import discord
from discord.ext import commands
import dormir
import asyncio
from datetime import datetime
import re
import time
from random import randint
import os

async def obtener_prefijo(bot, message):
    # Permite !comando y @Bot !comando
    if bot.user is None:
        return ["!"]

    return [
        "!",
        f"<@{bot.user.id}> !",
        f"<@!{bot.user.id}> !"
    ]


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True


class MiBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("commands.purgatorio")
        await self.load_extension("handlers.messages")
        await self.load_extension("commands.active")
        await self.load_extension("commands.changeid")

        asyncio.create_task(debug_sueno())

bot = MiBot(
    command_prefix=obtener_prefijo,
    intents=intents
)


@bot.check
async def comprobar_si_esta_despierta(ctx):
    return dormir.esta_despierta()

async def debug_sueno():
    await bot.wait_until_ready()

    while not bot.is_closed():
        dormida = dormir.esta_dormida()
        estado = "DORMIDA" if dormida else "DESPIERTA"

        print(
            f"[DEBUG SUEÑO] {estado} | "
            f"Hora: {datetime.now().strftime('%H:%M:%S')}"
        )

        await asyncio.sleep(1)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

        
bot.run(os.getenv("DISCORD_TOKEN"))
