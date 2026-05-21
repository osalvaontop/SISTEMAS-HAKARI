import discord
from discord.ext import commands

TICKET_IMAGE = ""  # coloque a imagem depois

class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Abrir Ticket", style=discord.ButtonStyle.green, emoji="🎫")
    async def ticket_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        guild = interaction.guild

        existing = discord.utils.get(guild.text_channels, name=f"ticket-{interaction.user.name}")

        if existing:
            await interaction.response.send_message(
                "Você já possui um ticket aberto.",
                ephemeral=True
            )
            return

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True
            )
        }

        channel = await guild.create_text_channel(
            name=f"ticket-{interaction.user.name}",
            overwrites=overwrites
        )

        embed = discord.Embed(
            title="🎫 Ticket Aberto",
            description="Explique seu problema e aguarde a equipe.",
            color=discord.Color.green()
        )

        await channel.send(
            content=interaction.user.mention,
            embed=embed
        )

        await interaction.response.send_message(
            f"Seu ticket foi criado: {channel.mention}",
            ephemeral=True
        )

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def painel(self, ctx):

        embed = discord.Embed(
            title="🎫 Sistema de Tickets",
            description="Clique no botão abaixo para abrir um ticket.",
            color=discord.Color.blurple()
        )

        if TICKET_IMAGE:
            embed.set_image(url=TICKET_IMAGE)

        await ctx.send(embed=embed, view=TicketView())

async def setup(bot):
    await bot.add_cog(Tickets(bot))
