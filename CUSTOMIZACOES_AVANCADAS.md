# 🎨 Guia de Customizações Avançadas

Este arquivo contém exemplos de como customizar o sistema de calls além das configurações básicas.

---

## 🎨 Customização 1: Alterar Cores dos Botões

No arquivo `cogs/calls.py`, procure a classe `ConfigCallView`:

```python
@discord.ui.button(label="Nome", style=discord.ButtonStyle.blurple, custom_id="config_nome")
async def nome_button(self, interaction: discord.Interaction, button: discord.ui.Button):
```

Altere `discord.ButtonStyle.blurple` para uma das opções:

```python
# Opções disponíveis:
discord.ButtonStyle.blurple    # Azul (padrão)
discord.ButtonStyle.gray       # Cinza
discord.ButtonStyle.green      # Verde
discord.ButtonStyle.red        # Vermelho
discord.ButtonStyle.secondary  # Cinza claro
```

**Exemplo - Botão Nome em Verde:**
```python
@discord.ui.button(label="Nome", style=discord.ButtonStyle.green, custom_id="config_nome")
```

---

## 🏷️ Customização 2: Alterar Labels dos Botões

No arquivo `cogs/calls.py`, na classe `ConfigCallView`, altere o `label`:

```python
# Antes:
@discord.ui.button(label="Nome", style=discord.ButtonStyle.blurple, custom_id="config_nome")

# Depois:
@discord.ui.button(label="✏️ Renomear", style=discord.ButtonStyle.blurple, custom_id="config_nome")
```

---

## 🎯 Customização 3: Alterar ID do Canal do Painel

No início do arquivo `cogs/calls.py`:

```python
# Antes:
PAINEL_CHANNEL_ID = 1507595486889115698

# Depois (altere para seu ID):
PAINEL_CHANNEL_ID = 1234567890123456789
```

Para obter o ID de um canal:
1. Ative o "Modo de Desenvolvedor" no Discord
2. Clique com botão direito no canal
3. Selecione "Copiar ID do Canal"

---

## 📝 Customização 4: Alterar Nome Padrão da Call

No arquivo `cogs/calls.py`, na função `criar_call_button`:

```python
# Antes:
nome_padrao = f"Call de {interaction.user.name}"

# Depois (exemplo):
nome_padrao = f"🎙️ {interaction.user.name}"
```

---

## 📢 Customização 5: Alterar Mensagens do Sistema

No arquivo `cogs/calls.py`, procure por `await interaction.followup.send()` e altere as mensagens.

**Exemplo - Mudar mensagem de sucesso ao criar call:**

```python
# Antes:
await interaction.followup.send(
    f"✅ Call criada com sucesso!\n**{nome_padrao}**\n\nUse `/configcall` para gerenciar sua call.",
    ephemeral=True
)

# Depois:
await interaction.followup.send(
    f"🎉 Sua call foi criada!\n**{nome_padrao}**\n\nDica: Use `/configcall` para personalizar!",
    ephemeral=True
)
```

---

## 🌈 Customização 6: Alterar Cores das Embeds

No arquivo `cogs/calls.py`, procure por `discord.Embed(..., color=discord.Color.xxx())`.

**Opções de cores:**

```python
discord.Color.blurple()    # Azul (padrão do Discord)
discord.Color.red()        # Vermelho
discord.Color.green()      # Verde
discord.Color.gold()       # Dourado
discord.Color.purple()     # Roxo
discord.Color.teal()       # Azul-verde
discord.Color.orange()     # Laranja
discord.Color.pink()       # Rosa
discord.Color.from_rgb(255, 100, 50)  # RGB personalizado
```

**Exemplo - Embed em vermelho:**

```python
# Antes:
embed = discord.Embed(
    title="🎙️ Sistema de Calls Personalizado",
    description="...",
    color=discord.Color.blurple()
)

# Depois:
embed = discord.Embed(
    title="🎙️ Sistema de Calls Personalizado",
    description="...",
    color=discord.Color.red()
)
```

---

## 🔧 Customização 7: Adicionar Novas Configurações

Para adicionar um novo botão de configuração, siga este exemplo:

**Passo 1: Criar um Modal (se necessário)**

```python
class MinhaCustomizacaoModal(discord.ui.Modal, title="Minha Customização"):
    valor = discord.ui.TextInput(
        label="Digite algo",
        placeholder="Placeholder aqui",
        required=False,
        max_length=100
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        
        calls_data = load_calls_data()
        user_id = str(interaction.user.id)
        
        if user_id not in calls_data:
            await interaction.followup.send("❌ Call não encontrada!", ephemeral=True)
            return
        
        # Sua lógica aqui
        calls_data[user_id]["meu_campo"] = self.valor.value
        save_calls_data(calls_data)
        
        await interaction.followup.send("✅ Salvo com sucesso!", ephemeral=True)
```

**Passo 2: Adicionar Botão na View**

```python
class ConfigCallView(discord.ui.View):
    # ... botões existentes ...
    
    @discord.ui.button(label="Meu Botão", style=discord.ButtonStyle.blurple, custom_id="meu_botao")
    async def meu_botao(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.show_modal(MinhaCustomizacaoModal())
```

---

## 📊 Customização 8: Adicionar Estatísticas

Para adicionar um campo de estatísticas na embed de configuração, edite a função `configcall`:

```python
# Antes:
embed.add_field(name="Limite", value=limite_texto, inline=True)
embed.add_field(name="Status", value=status_publica, inline=True)

# Depois:
embed.add_field(name="Limite", value=limite_texto, inline=True)
embed.add_field(name="Status", value=status_publica, inline=True)
embed.add_field(name="Pessoas", value=f"👥 {len(channel.members)}/10", inline=True)
```

---

## 🔔 Customização 9: Notificações Quando Alguém Entra na Call

Adicione este listener na classe `Calls`:

```python
@commands.Cog.listener()
async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    """Notifica quando alguém entra/sai de uma call"""
    calls_data = load_calls_data()
    
    # Se entrou em um canal de call
    if after.channel and after.channel.id in [int(data["channel_id"]) for data in calls_data.values()]:
        # Notificar que entrou
        print(f"✅ {member.name} entrou em uma call")
    
    # Se saiu de um canal de call
    if before.channel and before.channel.id in [int(data["channel_id"]) for data in calls_data.values()]:
        # Notificar que saiu
        print(f"👋 {member.name} saiu de uma call")
```

---

## 🎯 Customização 10: Deletar Calls Vazias Automaticamente

Modifique o listener `on_voice_state_update`:

```python
@commands.Cog.listener()
async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    """Deleta calls vazias automaticamente"""
    calls_data = load_calls_data()
    
    # Se o membro saiu de um canal
    if before.channel and not after.channel:
        # Verifica se a call está vazia
        for user_id, call_info in list(calls_data.items()):
            try:
                channel = self.bot.get_channel(int(call_info["channel_id"]))
                if channel and len(channel.members) == 0 and channel.id == before.channel.id:
                    # Deleta a call vazia após 5 minutos
                    await asyncio.sleep(300)  # 5 minutos
                    if len(channel.members) == 0:
                        await channel.delete()
                        del calls_data[user_id]
                        save_calls_data(calls_data)
            except:
                pass
```

---

## 🔐 Customização 11: Verificação de Permissões Avançada

Para permitir que apenas membros com um cargo específico criem calls:

```python
@app_commands.command(name="configcall", description="Gerencia sua call personalizada")
@app_commands.checks.has_role("Admin")  # Altere para seu nome de cargo
async def configcall(self, interaction: discord.Interaction):
    # ... resto da função ...
```

---

## 💾 Customização 12: Salvar Backup de Dados

Adicione esta função ao cog:

```python
@app_commands.command(name="backupcalls", description="Faz backup dos dados das calls")
@app_commands.checks.has_permissions(administrator=True)
async def backupcalls(self, interaction: discord.Interaction):
    import shutil
    from datetime import datetime
    
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"calls_backup_{timestamp}.json"
        shutil.copy(CALLS_DATA_FILE, backup_file)
        
        await interaction.response.send_message(
            f"✅ Backup criado: {backup_file}",
            ephemeral=True
        )
    except Exception as e:
        await interaction.response.send_message(f"❌ Erro ao criar backup: {e}", ephemeral=True)
```

---

## 🌐 Customização 13: Suporte a Múltiplos Servidores

Se o bot é usado em múltiplos servidores, considere usar diferentes IDs de canal por servidor:

```python
# Mapa de canais por servidor
PAINEL_CHANNELS = {
    123456789: 1507595486889115698,      # Server 1
    987654321: 1234567890123456789,      # Server 2
}

# Na função painelcall:
channel_id = PAINEL_CHANNELS.get(interaction.guild_id)
if not channel_id:
    await interaction.response.send_message(
        "❌ Servidor não configurado para este comando!",
        ephemeral=True
    )
    return
```

---

## 📈 Customização 14: Limite Máximo de Calls por Usuário

```python
# No botão de criar call
user_id = str(interaction.user.id)
calls_count = sum(1 for uid in calls_data.keys() if uid == user_id)

if calls_count >= 3:  # Máximo de 3 calls por usuário
    await interaction.followup.send(
        "❌ Você atingiu o limite máximo de calls!",
        ephemeral=True
    )
    return
```

---

## 🎪 Customização 15: Sistema de Permissões Compartilhadas

Para permitir que outros usuários gerenciem a call:

```python
# Adicione este campo ao salvar dados da call:
calls_data[user_id]["gerentes"] = [123456789, 987654321]  # IDs de outros gerentes

# Na função configcall, verifique:
if user_id != str(interaction.user.id):
    if interaction.user.id not in calls_data[user_id].get("gerentes", []):
        await interaction.response.send_message(
            "❌ Apenas o criador e gerentes podem configurar!",
            ephemeral=True
        )
        return
```

---

## 📚 Recursos Úteis

- [Discord.py Documentação](https://discordpy.readthedocs.io/)
- [Discord API Reference](https://discord.com/developers/docs/intro)
- [Discord.py Colors](https://discordpy.readthedocs.io/en/stable/api.html#discord.Color)
- [Discord.py Button Styles](https://discordpy.readthedocs.io/en/stable/api.html#discord.ButtonStyle)

---

## 🚀 Dicas Gerais

1. **Sempre faça backup** do arquivo `calls_data.json` antes de fazer grandes mudanças
2. **Teste em um servidor de teste** antes de implementar em produção
3. **Reinicie o bot** após fazer alterações no código
4. **Use try/except** para evitar crashes inesperados
5. **Registre seus logs** para debugging

---

**Divirta-se customizando! 🎉**
