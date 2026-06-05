# 🚀 Primeira Execução - Sistema de Calls

## ⚡ Pré-requisitos

Antes de começar, certifique-se de que:

- [x] Bot Discord criado no Discord Developer Portal
- [x] Token do bot configurado em `.env` ou variável de ambiente
- [x] Bot adicionado ao servidor com permissões necessárias
- [x] Python 3.8+ instalado
- [x] discord.py instalado (`pip install discord.py`)
- [x] Bot está online e respondendo

---

## 🔐 Permissões Necessárias do Bot

Seu bot deve ter estas permissões no servidor:

- ✅ **Enviar Mensagens**
- ✅ **Incorporar Links**
- ✅ **Gerenciar Canais**
- ✅ **Gerenciar Permissões**
- ✅ **Mover Membros**
- ✅ **Mudar Nick**

### Como verificar/adicionar:

1. Vá para o Discord Developer Portal
2. Navegue até `Applications` → Seu Bot
3. Clique em `OAuth2` → `URL Generator`
4. Selecione scopes: `bot`
5. Selecione permissões (as listadas acima)
6. Copie a URL e abra em seu navegador
7. Selecione o servidor e confirme

---

## 📋 Checklist Antes de Começar

- [ ] Bot está online e respondendo
- [ ] Bot tem todas as permissões necessárias
- [ ] Token está configurado corretamente
- [ ] Arquivo `cogs/calls.py` existe
- [ ] Servidor Discord está pronto para testes

---

## 🎯 Passo 1: Verificar Instalação

Verifique se o sistema foi instalado corretamente:

```bash
# 1. Verifique se o arquivo existe
ls cogs/calls.py
# Esperado: cogs/calls.py

# 2. Verifique se não há erros de sintaxe
python -m py_compile cogs/calls.py
# Esperado: Sem saída (significa OK)
```

---

## 🚀 Passo 2: Iniciar o Bot

```bash
# Certifique-se de estar no diretório certo
cd /workspaces/HAKARI-VOLTOU

# Inicie o bot
python app.py

# Procure por esta mensagem:
# ✅ Cog carregada: cogs.calls
# ✅ X slash commands sincronizados!
```

**Esperado:**
```
✅ Cog carregada: cogs.calls
✅ 4 slash commands sincronizados!
✅ Logado como HAKARI-VOLTOU#1234
```

Se não aparecer a mensagem sobre `calls`, reinicie o bot.

---

## 🎪 Passo 3: Enviar o Painel

Agora vamos enviar o painel de criação de calls:

1. **Abra o Discord**
2. **Vá para qualquer canal de texto** no seu servidor
3. **Digite:** `/painelcall`
4. **Pressione Enter**

**Esperado:**
- Uma mensagem de confirmação: "✅ Painel enviado com sucesso!"
- Uma embed no canal de ID `1507595486889115698` com um botão "Criar Call"

**Se não funcionou:**
- Verifique se você é admin
- Verifique se o bot tem permissão de "Enviar Mensagens"
- Verifique se o canal `1507595486889115698` existe

---

## 👤 Passo 4: Criar uma Call (Como Usuário)

Agora teste a criação de uma call:

1. **Abra o Discord**
2. **Vá até o canal com o painel** (onde foi enviado)
3. **Clique no botão "Criar Call"**

**Esperado:**
- Um novo canal de voz aparece com o nome: `Call de <seu_nome>`
- Você recebe uma mensagem: "✅ Call criada com sucesso!"

**Se não funcionou:**
- Verifique se o bot tem permissão "Gerenciar Canais"
- Verifique se você não já tem uma call ativa

---

## ⚙️ Passo 5: Configurar a Call

Agora vamos testar o menu de configuração:

1. **Digite:** `/configcall`
2. **Pressione Enter**

**Esperado:**
- Uma embed apareça com o título "⚙️ Configurar Call"
- 3 botões: "Nome", "Limite", "Pública"

### Teste 5A: Renomear (Botão "Nome")

1. **Clique no botão "Nome"**
2. **Um modal aparece** para você digitar o novo nome
3. **Digite:** `Meu Primeiro Chat`
4. **Clique em "Submit"**

**Esperado:**
- Mensagem de sucesso
- Canal é renomeado para "Meu Primeiro Chat"

### Teste 5B: Definir Limite (Botão "Limite")

1. **Clique no botão "Limite"**
2. **Um modal aparece** para você digitar um número
3. **Digite:** `5`
4. **Clique em "Submit"**

**Esperado:**
- Mensagem de sucesso
- Canal agora aceita máximo 5 pessoas

### Teste 5C: Alterar Privacidade (Botão "Pública")

1. **Clique no botão "Pública"**
2. **Botão muda de cor**: de verde para vermelho
3. **Mensagem:** "✅ Call definida como 🔴 Privada"

**Esperado:**
- Apenas você pode entrar na call
- Outros usuários recebem erro ao tentar entrar

**Teste novamente:**
1. **Clique novamente no botão "Privada"**
2. **Botão muda de cor**: de vermelho para verde
3. **Mensagem:** "✅ Call definida como 🟢 Pública"

**Esperado:**
- Qualquer pessoa agora pode entrar

---

## 📋 Passo 6: Listar Calls Ativas

Como admin, teste a listagem de calls:

1. **Digite:** `/listarcalls`
2. **Pressione Enter**

**Esperado:**
- Uma embed com título "📋 Calls Ativas"
- Sua call aparece na lista com informações:
  - Nome
  - Limite
  - Status (Pública/Privada)
  - Quantas pessoas estão conectadas

---

## 🗑️ Passo 7: Deletar a Call

Por último, teste a deleção:

1. **Digite:** `/deletarcall`
2. **Pressione Enter**

**Esperado:**
- Mensagem de sucesso: "✅ Call deletada com sucesso!"
- Canal de voz é deletado do Discord
- Dados são removidos

---

## 🔄 Teste Completo (Passo 1-7)

Se todos os passos acima funcionarem, seu sistema está **100% operacional**!

---

## ⚠️ Problemas Comuns e Soluções

### ❌ "Slash command não aparece"
**Solução:**
1. Reinicie o bot
2. Aguarde 30 segundos
3. Verifique a mensagem de sincronização no console

### ❌ "Erro: Você não possui permissão"
**Solução:**
1. Verifique se você é admin (para `/painelcall`)
2. Verifique se você é o criador da call (para `/configcall`)

### ❌ "Botões não funcionam após reinício"
**Solução:**
1. Reinicie o bot
2. Executar `/configcall` novamente

### ❌ "Canal não é criado"
**Solução:**
1. Verifique se o bot tem permissão "Gerenciar Canais"
2. Verifique se você não tem uma call ativa
3. Verifique se não há limite de canais no servidor

### ❌ "Arquivo calls_data.json não existe"
**Solução:**
1. Crie uma call - ele será criado automaticamente
2. Ou crie manualmente um arquivo vazio `{}`

---

## 📊 Verificação do Arquivo de Dados

Após criar uma call, verifique o arquivo `calls_data.json`:

```bash
# Ver conteúdo do arquivo
cat calls_data.json

# Esperado:
{
    "seu_id": {
        "channel_id": 123456789,
        "nome": "Call de Você",
        "limite": 5,
        "publica": false,
        "criador": seu_id
    }
}
```

---

## 📝 Próximos Passos

Após confirmar que tudo funciona:

1. **Leia** `SISTEMA_CALLS_DOCUMENTACAO.md` para documentação completa
2. **Siga** os testes em `TESTES_SYSTEM_CALLS.md` para testes mais completos
3. **Explore** `CUSTOMIZACOES_AVANCADAS.md` se quiser personalizar
4. **Use** `config_calls.py` para alterar mensagens e cores (opcional)

---

## 🎯 Quick Reference - Comandos

```
/painelcall      → Envia painel de criação (ADMIN)
/configcall      → Abre menu de configuração (CRIADOR)
/deletarcall     → Deleta sua call (CRIADOR)
/listarcalls     → Lista todas as calls (ADMIN)
```

---

## 📞 Suporte

Se algo não funcionar:

1. Verifique a mensagem de erro exata
2. Consulte "⚠️ Problemas Comuns e Soluções" acima
3. Leia `SISTEMA_CALLS_DOCUMENTACAO.md` seção "Resolução de Problemas"
4. Verifique permissões do bot
5. Reinicie o bot

---

## ✅ Checklist Final

- [ ] Bot iniciado com sucesso
- [ ] Cog `calls` carregada
- [ ] `/painelcall` enviou o painel
- [ ] Botão "Criar Call" funciona
- [ ] `/configcall` abre menu
- [ ] Botão "Nome" funciona
- [ ] Botão "Limite" funciona
- [ ] Botão "Pública/Privada" funciona
- [ ] `/deletarcall` funciona
- [ ] `/listarcalls` funciona
- [ ] Arquivo `calls_data.json` foi criado

---

## 🎉 Conclusão

Se todos os itens do checklist acima estão marcados, seu sistema está **pronto para produção**!

Divirta-se com o novo sistema de calls! 🚀

---

**Próxima leitura:** Abra `SISTEMA_CALLS_DOCUMENTACAO.md` para saber mais sobre cada funcionalidade.

**Desenvolvido com ❤️ para HAKARI-VOLTOU**
