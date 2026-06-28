import discord
from discord.ext import commands, tasks

VOICE_CHANNEL_ID = 1512845054450991115

class VoiceStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.keep_voice.start()

    def cog_unload(self):
        self.keep_voice.cancel()

    @tasks.loop(seconds=15)
    async def keep_voice(self):
        channel = self.bot.get_channel(VOICE_CHANNEL_ID)

        if channel is None:
            print("Canal não encontrado. ID errado ou bot não vê o canal.")
            return

        if not isinstance(channel, discord.VoiceChannel):
            print(f"Esse ID não é canal de voz. Tipo encontrado: {type(channel)}")
            return

        guild = channel.guild
        vc = guild.voice_client

        try:
            if vc is None:
                print(f"Tentando conectar em: {channel.name}")
                await channel.connect(self_deaf=True)
                print("Conectado com sucesso.")

            elif vc.channel.id != VOICE_CHANNEL_ID:
                print(f"Movendo para: {channel.name}")
                await vc.move_to(channel)

        except discord.Forbidden:
            print("Sem permissão pra conectar nesse canal.")
        except discord.ClientException as e:
            print(f"Erro do client: {e}")
        except Exception as e:
            print(f"Erro desconhecido: {type(e).__name__}: {e}")

    @keep_voice.before_loop
    async def before_keep_voice(self):
        await self.bot.wait_until_ready()


async def setup(bot):
    await bot.add_cog(VoiceStatus(bot))
