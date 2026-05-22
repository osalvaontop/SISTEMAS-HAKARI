import discord
import time
import random
from discord.ext import commands

cooldowns = {}

class Tomato(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tomate(self, ctx):

        if not ctx.author.guild_permissions.administrator:

            last_used = cooldowns.get(ctx.author.id)

            if last_used:
                remaining = 1200 - (time.time() - last_used)

                if remaining > 0:
                    await ctx.send(
                        f"⏳ Espere {int(remaining)} segundos para usar novamente."
                    )
                    return

            cooldowns[ctx.author.id] = time.time()

        messages = [msg async for msg in ctx.channel.history(limit=6)]
        messages = [msg for msg in messages if msg.id != ctx.message.id][:5]

        if messages:
            selected_msg = random.choice(messages)
            try:
                await selected_msg.add_reaction("🍅")
            except Exception:
                pass

        await ctx.send("🍅 O tomate foi lançado.")

async def setup(bot):
    await bot.add_cog(Tomato(bot))
