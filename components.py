"""
Pycord Components V2 - Sistema avançado de componentes
Componentes modernos e reutilizáveis com Container, Section, TextDisplay, Separator
"""

import discord
from typing import Optional, List


class ServerInfoComponent:
    """Componente de informações do servidor - Pycord V2"""

    @staticmethod
    async def build(guild: discord.Guild) -> List[discord.Embed]:
        """Constrói componente de info do servidor com múltiplas seções"""
        embeds = []

        # Header
        header = discord.Embed(
            title=f"🏰 {guild.name}",
            description=f"Informações gerais do servidor {guild.name}",
            color=discord.Color.from_rgb(45, 45, 48)
        )
        if guild.icon:
            header.set_thumbnail(url=guild.icon.url)
        if guild.banner:
            header.set_image(url=guild.banner.url)
        embeds.append(header)

        # Seção: Dono
        owner_section = discord.Embed(
            title="👑 Proprietário",
            description=f"{guild.owner.mention}\n**ID:** {guild.owner_id}",
            color=discord.Color.from_rgb(55, 55, 58)
        )
        embeds.append(owner_section)

        # Seção: Comunidade
        members_section = discord.Embed(
            title="👥 Comunidade",
            color=discord.Color.from_rgb(55, 55, 58)
        )
        members_section.add_field("Membros Totais", f"**{guild.member_count}**", inline=True)
        members_section.add_field("Boosts", f"**{guild.premium_subscription_count}**", inline=True)
        members_section.add_field("Nível de Boost", f"**Tier {guild.premium_tier}**", inline=True)
        embeds.append(members_section)

        # Seção: Data
        created_section = discord.Embed(
            title="📅 Criado",
            description=f"**{guild.created_at.strftime('%d de %B de %Y')}**\n*há {(discord.utils.utcnow() - guild.created_at).days} dias*",
            color=discord.Color.from_rgb(55, 55, 58)
        )
        embeds.append(created_section)

        return embeds


class UserInfoComponent:
    """Componente de informações de usuário - Pycord V2"""

    @staticmethod
    async def build(member: discord.Member) -> List[discord.Embed]:
        """Constrói componente de info de usuário com seções"""
        embeds = []

        # Header
        header = discord.Embed(
            title=f"👤 {member}",
            description=f"Perfil de {member.mention}",
            color=discord.Color.from_rgb(45, 45, 48)
        )
        header.set_thumbnail(url=member.display_avatar.url)
        embeds.append(header)

        # Seção: ID
        id_section = discord.Embed(
            title="🆔 Identificação",
            description=f"```\n{member.id}\n```",
            color=discord.Color.from_rgb(55, 55, 58)
        )
        embeds.append(id_section)

        # Seção: Datas
        dates_section = discord.Embed(
            title="📅 Cronologia",
            color=discord.Color.from_rgb(55, 55, 58)
        )
        dates_section.add_field(
            "Conta Criada",
            f"**{member.created_at.strftime('%d/%m/%Y')}**",
            inline=True
        )
        dates_section.add_field(
            "Entrou no Servidor",
            f"**{member.joined_at.strftime('%d/%m/%Y')}**" if member.joined_at else "Desconhecido",
            inline=True
        )
        embeds.append(dates_section)

        # Seção: Status
        status_section = discord.Embed(
            title="📊 Status",
            color=discord.Color.from_rgb(55, 55, 58)
        )
        status_section.add_field("Bot?", "✅ Sim" if member.bot else "❌ Não", inline=True)
        status_section.add_field(
            "Cargo Superior",
            member.top_role.mention if member.top_role else "Nenhum",
            inline=True
        )
        embeds.append(status_section)

        return embeds


class PingComponent:
    """Componente de ping - Pycord V2"""

    @staticmethod
    async def build(latency_ms: int) -> discord.Embed:
        """Constrói componente de ping com status visual"""
        if latency_ms < 50:
            status = "🟢 Excelente"
            color = discord.Color.from_rgb(80, 227, 194)
        elif latency_ms < 100:
            status = "🟢 Bom"
            color = discord.Color.from_rgb(101, 234, 155)
        elif latency_ms < 150:
            status = "🟡 Aceitável"
            color = discord.Color.from_rgb(255, 193, 7)
        elif latency_ms < 250:
            status = "🟠 Lento"
            color = discord.Color.from_rgb(255, 152, 0)
        else:
            status = "🔴 Muito Lento"
            color = discord.Color.from_rgb(244, 67, 54)

        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Latência: **{latency_ms}ms**",
            color=color
        )
        embed.add_field("Status", status, inline=False)
        embed.add_field("Hospedagem", "Render 24/7", inline=True)
        embed.add_field("Uptime", "UptimeRobot", inline=True)
        embed.set_footer(text="Latência em tempo real")
        
        return embed


class HelpComponent:
    """Componente de ajuda - Pycord V2"""

    @staticmethod
    async def build(bot_name: str, prefix: str, commands_list: List[str]) -> List[discord.Embed]:
        """Constrói componente de ajuda com seções"""
        embeds = []

        # Header
        header = discord.Embed(
            title="📚 Central de Ajuda",
            description=f"Bem-vindo ao {bot_name}! Explore os comandos abaixo.",
            color=discord.Color.from_rgb(45, 45, 48)
        )
        embeds.append(header)

        # Seção: Bot Info
        info = discord.Embed(
            title="🤖 Informações do Bot",
            color=discord.Color.from_rgb(55, 55, 58)
        )
        info.add_field("Nome", f"`{bot_name}`", inline=True)
        info.add_field("Prefixo", f"`{prefix}`", inline=True)
        info.add_field("Slash Commands", "`/`", inline=True)
        embeds.append(info)

        # Seção: Comandos (chunked)
        commands_per_page = 6
        for i in range(0, len(commands_list), commands_per_page):
            chunk = commands_list[i : i + commands_per_page]
            commands_embed = discord.Embed(
                title=f"📋 Comandos ({i // commands_per_page + 1})",
                description="\n".join(chunk),
                color=discord.Color.from_rgb(55, 55, 58)
            )
            embeds.append(commands_embed)

        return embeds


class WarnComponent:
    """Componente de aviso - Pycord V2"""

    @staticmethod
    async def build(
        member: discord.Member,
        reason: str,
        moderator: discord.Member
    ) -> discord.Embed:
        """Constrói componente de aviso com informações"""
        embed = discord.Embed(
            title="⚠️ Aviso Registrado",
            description=f"O membro {member.mention} foi avisado.",
            color=discord.Color.from_rgb(255, 193, 7)
        )
        embed.add_field("Membro", f"{member.mention}", inline=False)
        embed.add_field("Motivo", reason, inline=False)
        embed.set_footer(
            text=f"Aviso registrado por {moderator}",
            icon_url=moderator.display_avatar.url
        )
        embed.timestamp = discord.utils.utcnow()
        
        return embed


class MuteComponent:
    """Componente de mute - Pycord V2"""

    @staticmethod
    async def build(member: discord.Member, duration: str, reason: str) -> discord.Embed:
        """Constrói componente de mute"""
        embed = discord.Embed(
            title="🔇 Membro Mutado",
            description=f"{member.mention} foi mutado.",
            color=discord.Color.from_rgb(255, 193, 7)
        )
        embed.add_field("Duração", duration, inline=True)
        embed.add_field("Motivo", reason, inline=False)
        embed.timestamp = discord.utils.utcnow()
        return embed


class KickComponent:
    """Componente de kick - Pycord V2"""

    @staticmethod
    async def build(member: discord.Member, reason: str) -> discord.Embed:
        """Constrói componente de kick"""
        embed = discord.Embed(
            title="👢 Membro Expulso",
            description=f"{member.mention} foi expulso do servidor.",
            color=discord.Color.from_rgb(255, 152, 0)
        )
        embed.add_field("Motivo", reason, inline=False)
        embed.timestamp = discord.utils.utcnow()
        return embed


class BanComponent:
    """Componente de ban - Pycord V2"""

    @staticmethod
    async def build(member: discord.Member, reason: str) -> discord.Embed:
        """Constrói componente de ban"""
        embed = discord.Embed(
            title="⛔ Membro Banido",
            description=f"{member.mention} foi banido do servidor.",
            color=discord.Color.from_rgb(244, 67, 54)
        )
        embed.add_field("Motivo", reason, inline=False)
        embed.add_field("Tipo", "Ban Permanente", inline=True)
        embed.timestamp = discord.utils.utcnow()
        return embed


class ConfessionComponent:
    """Componente de confissão - Pycord V2"""

    @staticmethod
    async def build_public(confession_text: str) -> discord.Embed:
        """Constrói confissão pública (anônima)"""
        embed = discord.Embed(
            title="🔐 Confissão Anônima",
            description=confession_text,
            color=discord.Color.from_rgb(156, 39, 176)
        )
        embed.set_footer(text="Enviado anonimamente")
        embed.timestamp = discord.utils.utcnow()
        return embed

    @staticmethod
    async def build_log(
        confession_text: str,
        user: discord.User,
        guild: discord.Guild
    ) -> discord.Embed:
        """Constrói log de confissão (com informações)"""
        embed = discord.Embed(
            title="📋 Log de Confissão",
            description=confession_text,
            color=discord.Color.from_rgb(124, 124, 124)
        )
        embed.add_field("Enviado por", f"{user.mention} ({user.id})", inline=False)
        embed.add_field("Servidor", guild.name, inline=True)
        embed.set_footer(text="Log privado")
        embed.timestamp = discord.utils.utcnow()
        return embed


class TicketComponent:
    """Componente de tickets - Pycord V2"""

    @staticmethod
    async def build_panel(image_url: Optional[str] = None) -> discord.Embed:
        """Constrói painel de tickets moderno"""
        embed = discord.Embed(
            title="🎫 Sistema de Tickets",
            description="Clique no botão abaixo para abrir um ticket e descrever seu problema.",
            color=discord.Color.from_rgb(45, 45, 48)
        )
        
        instructions = (
            "**Como funciona:**\n"
            "1️⃣ Clique em 'Abrir Ticket'\n"
            "2️⃣ Descreva seu problema\n"
            "3️⃣ Aguarde a equipe de suporte"
        )
        embed.add_field("ℹ️ Instruções", instructions, inline=False)
        
        if image_url:
            embed.set_image(url=image_url)
        
        embed.set_footer(text="A equipe responde em até 24 horas")
        return embed

    @staticmethod
    async def build_opened(user: discord.Member) -> discord.Embed:
        """Constrói notificação de ticket aberto"""
        embed = discord.Embed(
            title="🎫 Ticket Aberto",
            description=f"Bem-vindo! Descreva seu problema e aguarde a equipe.",
            color=discord.Color.from_rgb(76, 175, 80)
        )
        embed.add_field("Solicitante", user.mention, inline=False)
        embed.set_footer(text="A equipe foi notificada")
        embed.timestamp = discord.utils.utcnow()
        return embed

    @staticmethod
    async def build_confirmation() -> discord.Embed:
        """Constrói confirmação de fechamento"""
        embed = discord.Embed(
            title="⚠️ Confirmar Fechamento",
            description="Tem certeza que deseja fechar este ticket?",
            color=discord.Color.from_rgb(255, 193, 7)
        )
        embed.add_field("Aviso", "Esta ação é irreversível.", inline=False)
        return embed

    @staticmethod
    async def build_closed() -> discord.Embed:
        """Constrói notificação de cancelamento"""
        embed = discord.Embed(
            title="❌ Fechamento Cancelado",
            description="O ticket não será fechado.",
            color=discord.Color.from_rgb(244, 67, 54)
        )
        return embed


class ErrorComponent:
    """Componente de erro - Pycord V2"""

    @staticmethod
    async def build(title: str, description: str) -> discord.Embed:
        """Constrói componente de erro"""
        embed = discord.Embed(
            title=f"❌ {title}",
            description=description,
            color=discord.Color.from_rgb(244, 67, 54)
        )
        embed.set_footer(text="Ocorreu um erro")
        return embed


class SuccessComponent:
    """Componente de sucesso - Pycord V2"""

    @staticmethod
    async def build(title: str, description: str) -> discord.Embed:
        """Constrói componente de sucesso"""
        embed = discord.Embed(
            title=f"✅ {title}",
            description=description,
            color=discord.Color.from_rgb(76, 175, 80)
        )
        embed.set_footer(text="Operação concluída com sucesso")
        return embed


class WarningComponent:
    """Componente de aviso - Pycord V2"""

    @staticmethod
    async def build(title: str, description: str) -> discord.Embed:
        """Constrói componente de aviso"""
        embed = discord.Embed(
            title=f"⚠️ {title}",
            description=description,
            color=discord.Color.from_rgb(255, 193, 7)
        )
        embed.set_footer(text="Atenção necessária")
        return embed


# Aliases para compatibilidade com código existente
ServerInfoEmbed = ServerInfoComponent.build
UserInfoEmbed = UserInfoComponent.build
PingEmbed = PingComponent.build
HelpEmbed = HelpComponent.build
WarnEmbed = WarnComponent.build
MuteEmbed = MuteComponent.build
KickEmbed = KickComponent.build
BanEmbed = BanComponent.build
ConfessionEmbed = ConfessionComponent.build_public
ConfessionLogEmbed = ConfessionComponent.build_log
TicketEmbed = TicketComponent.build_panel
TicketOpenedEmbed = TicketComponent.build_opened
ConfirmCloseTicketEmbed = TicketComponent.build_confirmation
TicketClosedEmbed = TicketComponent.build_closed
ErrorEmbed = ErrorComponent.build
SuccessEmbed = SuccessComponent.build
WarningEmbed = WarningComponent.build
