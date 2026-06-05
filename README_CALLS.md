# 🎙️ Sistema de Calls Personalizado - Quick Start

## ✅ Instalação

O sistema já está instalado! O arquivo `cogs/calls.py` foi criado e carregado automaticamente pelo bot.

### Passos após a criação:

1. **Reinicie o bot** para garantir que o cog seja carregado
2. **Tudo pronto!** O sistema está ativo e funcional

---

## 🚀 Primeiros Passos

### 1. Enviar o Painel

Um administrador deve executar o comando:

```
/painelcall
```

Este comando envia um painel interativo no canal `#calls` (ID: 1507595486889115698).

### 2. Usuários Criam Calls

Usuários clicam no botão "Criar Call" e um canal de voz é criado automaticamente.

### 3. Gerenciar a Call

Usuários executam `/configcall` para gerenciar:
- **Nome da call** (com botão "Nome")
- **Limite de pessoas** (com botão "Limite")
- **Privacidade** (com botão "Pública/Privada")

---

## 📋 Comandos Disponíveis

| Comando | Descrição | Permissão |
|---------|-----------|-----------|
| `/painelcall` | Envia o painel de criação | Admin |
| `/configcall` | Abre o menu de configuração | Apenas criador |
| `/deletarcall` | Deleta sua call | Apenas criador |
| `/listarcalls` | Lista todas as calls ativas | Admin |

---

## 🎯 Arquivos Criados

- `cogs/calls.py` - Sistema principal de calls
- `calls_data.json` - Arquivo de dados (criado automaticamente)
- `config_calls.py` - Arquivo de configurações (opcional)
- `SISTEMA_CALLS_DOCUMENTACAO.md` - Documentação completa

---

## ⚙️ Configurações Importantes

Se precisar alterar o **ID do canal do painel**, edite o arquivo `cogs/calls.py`:

```python
PAINEL_CHANNEL_ID = 1507595486889115698  # ← Altere este número
```

---

## 🔄 Sincronização de Comandos

Os comandos são sincronizados automaticamente quando o bot inicia. Você verá uma mensagem como:

```
✅ X slash commands sincronizados!
```

Se os comandos não aparecerem, reinicie o bot.

---

## 📝 Exemplo de Uso Completo

```
1. Admin: /painelcall
   → Painel aparece no canal

2. Usuário: Clica em "Criar Call"
   → Call criada: "Call de Maria"

3. Usuário: /configcall
   → Embed com 3 botões aparece

4. Usuário: Clica em "Nome"
   → Modal abre para digitar novo nome
   → Digita: "Estudo de Python"
   → Nome atualizado!

5. Usuário: Clica em "Limite"
   → Modal abre para digitar limite
   → Digita: "5"
   → Limite definido para 5 pessoas!

6. Usuário: Clica em "Pública"
   → Botão fica vermelho
   → Call agora é privada (só o criador entra)

7. Usuário: /deletarcall
   → Call deletada e dados removidos
```

---

## 🔧 Troubleshooting

### ❌ Comandos não aparecem
**Solução:** Reinicie o bot e aguarde 30 segundos.

### ❌ Botões não funcionam
**Solução:** Reinicie o bot. As views precisam ser re-registradas.

### ❌ Erro ao criar call
**Solução:** Verifique se o bot tem permissão para "Gerenciar Canais".

### ❌ Arquivo calls_data.json não aparece
**Solução:** Será criado automaticamente na primeira call.

---

## 📂 Estrutura de Diretórios

```
/workspaces/HAKARI-VOLTOU/
├── app.py
├── cogs/
│   ├── calls.py ← Sistema de calls
│   ├── admin.py
│   └── ...
├── config_calls.py
├── calls_data.json (criado automaticamente)
├── SISTEMA_CALLS_DOCUMENTACAO.md
└── README.md (este arquivo)
```

---

## 🎓 Próximas Etapas

- Leia `SISTEMA_CALLS_DOCUMENTACAO.md` para documentação completa
- Customize as mensagens em `config_calls.py` (opcional)
- Teste todos os comandos com um usuário de teste

---

## 💡 Dicas

- Use `/listarcalls` para monitorar todas as calls ativas
- Calls vazias não são deletadas automaticamente (isso é intencional)
- Os dados são salvos em tempo real no arquivo `calls_data.json`
- Apenas slash commands (`/`) funcionam - prefixos (`~`, `,`) não funcionam

---

**Desenvolvido com ❤️ para HAKARI-VOLTOU**
