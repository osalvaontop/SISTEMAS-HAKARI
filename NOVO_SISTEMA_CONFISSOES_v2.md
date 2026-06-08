# 🔐 NOVO SISTEMA DE CONFISSÕES v2.0

## 📌 Resumo das Alterações

O sistema de confissões foi completamente renovado com novas funcionalidades:

✅ **Respostas anônimas** - Membros podem responder confissões  
✅ **Denúncias** - Botão para denunciar confissões inapropriadas  
✅ **Sistema de moderação completo** - Avisar, castigar, expulsar, banir  
✅ **Permissões verificadas** - Cada ação valida permissões do moderador  
✅ **Logs detalhados** - Todas as ações são registradas

---

## 🎮 Como Funciona

### 1️⃣ Enviar Confissão (Usuário)

```
Usuário digita: /confissao
  ↓
Abre modal de formulário
  ↓
Escreve a confissão
  ↓
Embed aparece em 1507592685282787421 com 2 botões
```

### 2️⃣ Responder Confissão (Qualquer Membro)

```
Clica no botão 💬 "Responder"
  ↓
Abre modal de resposta
  ↓
Escreve a resposta
  ↓
Nova embed aparece com:
  - "confissão: <texto original>"
  - "respondendo para: [link]"
  - "resposta: <texto>"
  ↓
Resposta aparece identificada (não é anônima)
```

### 3️⃣ Denunciar Confissão (Qualquer Membro)

```
Clica no botão ⚠️ "Denunciar"
  ↓
Incrementa contador de denúncias
  ↓
Envia para canal 1490679538299043948
  ↓
Menciona cargo 1500969290093039626
  ↓
Embed mostra:
  - Confissão denunciada
  - Quem denunciou
  - Link para a confissão
  - Contador de denúncias
  - Select Menu de moderação
```

### 4️⃣ Moderar Confissão (Moderadores)

Clica no Select Menu "abrir caso de moderação" e escolhe:

#### 🟡 **Avisar** (precisa `moderate_members`)

```
Abre modal para escrever motivo
  ↓
Tenta enviar DM ao usuário
  ↓
Se DM fechada → envia no chat público
  ↓
Registra em logs
```

#### 🔇 **Castigar** (precisa `moderate_members`)

```
Abre modal para inserir tempo
  ↓
Formatos aceitos:
  - 1h   (1 hora)
  - 30m  (30 minutos)
  - 1d   (1 dia)
  - 5s   (5 segundos)
  - DD/MM/YYYY HH:MM (horário específico)
  ↓
Aplica timeout no usuário
  ↓
Registra em logs
```

#### 👢 **Expulsar** (precisa `kick_members`)

```
Clica na opção
  ↓
Remove usuário do servidor
  ↓
Registra em logs
```

#### 🔨 **Banir** (precisa `ban_members`)

```
Clica na opção
  ↓
Bane usuário permanentemente
  ↓
Registra em logs
```

---

## 🔑 Permissões Necessárias

| Ação | Permissão Necessária |
|------|----------------------|
| Avisar | `moderate_members` |
| Castigar (mute) | `moderate_members` |
| Expulsar (kick) | `kick_members` |
| Banir | `ban_members` |

**Comportamento:** Se o moderador não tiver a permissão, o botão fica indisponível com mensagem de erro.

---

## 📦 Detalhes Técnicos

### Constantes Importantes

```python
LOGS_CHANNEL_ID = 1490679538559221770           # Logs gerais
CONFISSOES_CHANNEL_ID = 1507592685282787421    # Onde as confissões aparecem
DENUNCIAS_CHANNEL_ID = 1490679538299043948     # Onde denúncias aparecem
MODERACAO_ROLE_ID = 1500969290093039626       # Cargo mencionado em denúncias
```

### Classes Adicionadas

1. **RespostaConfissaoModal** - Modal para responder confissões
2. **AvisoModal** - Modal para avisos com motivo
3. **CastigoModal** - Modal para aplicar timeout
4. **ConfissaoButtonsView** - View com botões Responder e Denunciar
5. **ModeracaoView** - View com Select Menu de ações

### Estrutura de Dados

```python
confissoes_map = {
    message_id: {
        "author_id": 123456789,
        "confissao_text": "texto da confissão",
        "reported": False,
        "reports": 0
    }
}
```

---

## 🔒 Segurança

✅ **Verificação de permissões** em cada ação de moderação  
✅ **Rastreamento de confissões** para impedir abuso  
✅ **Logs detalhados** de todas as ações  
✅ **Proteção contra múltiplas denúncias** (contador aumenta)  
✅ **Validação de entrada** em modais

---

## ⚙️ Setup Necessário

1. **Canais já devem existir:**
   - 1490679538559221770 (logs)
   - 1507592685282787421 (confissões)
   - 1490679538299043948 (denúncias)

2. **Cargo já deve existir:**
   - 1500969290093039626 (moderação)

3. **Bot deve ter permissões:**
   - Gerenciar usuários (timeout)
   - Expulsar membros
   - Banir membros
   - Enviar mensagens
   - Incorporar conteúdo

---

## 📝 Exemplos de Uso

### Exemplo 1: Confissão com Resposta

```
Usuario1: /confissao
  → "Eu tenho medo de falar em público"
  
Usuario2: Clica "Responder"
  → "Eu também! A prática ajuda muito"
  → Aparece embed com: confissão original + resposta
```

### Exemplo 2: Confissão Inapropriada

```
Usuario1: /confissao
  → "Confissão imprópria..."
  
Usuario2: Clica "Denunciar"
  → Envia para 1490679538299043948
  → Menciona @Moderadores
  
Moderador: Abre Select Menu
  → Escolhe "Banir"
  → Usuario1 é banido permanentemente
```

---

## 🐛 Troubleshooting

**Problema:** Botões não aparecem nas confissões  
**Solução:** Reiniciar bot com `python app.py` - views precisam ser registradas

**Problema:** "Sem permissão para avisar"  
**Solução:** Verificar se o moderador tem `moderate_members`

**Problema:** Timeout não funciona  
**Solução:** Verificar se bot tem permissão "Gerenciar usuários"

---

## 📊 Fluxograma Completo

```
START
  ↓
Usuário clica /confissao
  ↓
[ConfissaoModal] ← Escreve confissão
  ↓
Embed enviada com botões
  ├─→ 💬 Responder
  │    ↓
  │    [RespostaConfissaoModal]
  │    ↓
  │    Nova embed com link
  │
  └─→ ⚠️ Denunciar
       ↓
       Envia para canal 1490679538299043948
       ↓
       [ModeracaoView - Select Menu]
       ├─→ ⚠️ Avisar [AvisoModal]
       ├─→ 🔇 Castigar [CastigoModal]
       ├─→ 👢 Expulsar
       └─→ 🔨 Banir
       ↓
       Todas as ações → Logs em 1490679538559221770
```

---

## ✅ Checklist de Implementação

- ✅ Modals para respostas e moderação
- ✅ Botões Responder (verde) e Denunciar (vermelho)
- ✅ Select Menu com 4 ações de moderação
- ✅ Verificação de permissões para cada ação
- ✅ Sistema de duração para timeout (múltiplos formatos)
- ✅ DM ou chat público para avisos
- ✅ Logs de todas as ações
- ✅ Rastreamento de confissões e denúncias
- ✅ Views persistentes entre reinicializações

---

**Data de Implementação:** 2026-06-08  
**Versão:** 2.0  
**Status:** ✅ COMPLETO
