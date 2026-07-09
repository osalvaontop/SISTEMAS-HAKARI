import discord
from discord.ext import commands
from discord import app_commands

TICKET_IMAGE = "https://i.postimg.cc/ZRptsfK0/download-(2).gif"
SUPPORT_ROLE_ID = 1504998108407398501


class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="abrir ticket", style=discord.ButtonStyle.green, emoji="🎫")
    async def ticket_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)

        guild = interaction.guild

        existing = discord.utils.get(
            guild.text_channels,
            name=f"ticket-{interaction.user.name}".lower()
        )

        if existing:
            await interaction.followup.send(
                "você já possui um ticket aberto",
                ephemeral=True
            )
            return

        support_role = guild.get_role(SUPPORT_ROLE_ID)

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                read_message_history=True
            )
        }

        if support_role:
            overwrites[support_role] = discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                manage_messages=True,
                read_message_history=True
            )

        channel = await guild.create_text_channel(
            name=f"ticket-{interaction.user.name}".lower(),
            overwrites=overwrites,
            description=f"ID do usuário: {interaction.user.id}"
        )

        embed = discord.Embed(
            title="ticket aberto",
            description=(
                "ㅤㅤㅤㅤㅤㅤㅤㅤ  ㅤ__***boas vindas ao seu ticket!***__\n"
                "ㅤㅤㅤ__***explique o motivo do seu ticket abaixo, enquanto aguarda a equipe.***__"
            ),
            color=0xffffff
        )
        embed.set_image(url="https://i.postimg.cc/MGv7qV15/download-(1).gif")

        mention_text = interaction.user.mention

        if support_role:
            mention_text += f" {support_role.mention}"

        await channel.send(
            content=mention_text,
            embed=embed
        )

        await interaction.followup.send(
            f"seu ticket foi criado: {channel.mention}",
            ephemeral=True
        )


class CloseTicketView(discord.ui.View):
    def __init__(self, channel):
        super().__init__(timeout=None)
        self.channel = channel

    @discord.ui.button(label="confirmar", style=discord.ButtonStyle.green, emoji="✅")
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.channel.delete()

    @discord.ui.button(label="cancelar", style=discord.ButtonStyle.red, emoji="❌")
    async def cancel_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="cancelado",
            description="ticket não será fechado",
            color=discord.Color.red()
        )
        embed.set_footer(
            text="se tu quiser fechar ele agora é só rodar o mesmo comando e clicar em confirmar"
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)
        self.stop()


class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="painel")
    @commands.has_permissions(administrator=True)
    async def painel_prefix(self, ctx):
        embed = discord.Embed(
            title=".",
            description=(
                "ㅤㅤㅤㅤㅤㅤ__***boas vindas ao sistema de tickets!***__\n\n"
                "ㅤㅤㅤㅤㅤㅤㅤㅤㅤ__***aqui você pode ter o seu suporte envolvendo coisas do servidor.***__\n\n"
                "ㅤㅤㅤ__***sinta-se à vontade para ser atendido pela equipe.***__"
            ),
            color=0xffffff
        )

        if TICKET_IMAGE:
            embed.set_image(url=TICKET_IMAGE)

        await ctx.send(embed=embed, view=TicketView())

    @app_commands.command(name="painel", description="Envia o painel de tickets")
    @app_commands.checks.has_permissions(administrator=True)
    async def painel_slash(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🎫 sistema de tickets",
            description="clique no botão abaixo para abrir um ticket",
            color=discord.Color.blurple()
        )

        if TICKET_IMAGE:
            embed.set_image(url=TICKET_IMAGE)

        await interaction.response.send_message(embed=embed, view=TicketView())

    @commands.command(name="fechar")
    async def fechar_prefix(self, ctx):
        if not ctx.channel.name.startswith("ticket-"):
            embed = discord.Embed(
                title="❌ erro",
                description="este comando só pode ser usado em canais de ticket",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        support_role = ctx.guild.get_role(SUPPORT_ROLE_ID)

        if support_role not in ctx.author.roles:
            embed = discord.Embed(
                title="❌ epa pera aí amigão",
                description="só administradores podem fechar o ticket",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(
            title="⚠️ confirmação de fechamento",
            description="quer mesmo fechar este ticket?",
            color=discord.Color.yellow()
        )

        await ctx.send(embed=embed, view=CloseTicketView(ctx.channel))

    @app_commands.command(name="fechar", description="Fecha um ticket")
    async def fechar_slash(self, interaction: discord.Interaction):
        if not interaction.channel.name.startswith("ticket-"):
            embed = discord.Embed(
                title="❌ erro",
                description="este comando só pode ser usado em canais de ticket!",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        support_role = interaction.guild.get_role(SUPPORT_ROLE_ID)

        if support_role not in interaction.user.roles:
            embed = discord.Embed(
                title="❌ pera aí",
                description="só administradores podem fechar o ticket",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        embed = discord.Embed(
            title="⚠️ confirmação de fechamento",
            description="tem certeza que deseja fechar este ticket?",
            color=discord.Color.yellow()
        )

        await interaction.response.send_message(
            embed=embed,
            view=CloseTicketView(interaction.channel),
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Tickets(bot))
