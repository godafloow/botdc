import dormir
from discord.ext import commands
from commands.mencion import gestionar_mencion

class MessageHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if not dormir.esta_despierta():
            await dormir.intentar_despertar(message)
            return
        
        
        # Aquí puedes añadir lógica general para mensajes.
        # No procesamos los comandos aquí para evitar duplicarlos.
        pass
        if self.bot.user in message.mentions:
            await gestionar_mencion(message, self.bot)


async def setup(bot):
    await bot.add_cog(MessageHandler(bot))
