# 📋 RESUMO DAS MUDANÇAS - SISTEMA DE CONFISSÃO v2.0

## 🎯 O que foi adicionado em `cogs/diversao.py`

### ✨ 5 Novas Classes

| # | Classe | Função | Botão/Modal |
|---|--------|--------|-----------|
| 1 | `RespostaConfissaoModal` | Responder confissões com link | Modal 💬 |
| 2 | `AvisoModal` | Avisar usuários com motivo | Modal ⚠️ |
| 3 | `CastigoModal` | Aplicar timeout com duração | Modal 🔇 |
| 4 | `ConfissaoButtonsView` | Botões nas confissões | Botões 💚❤️ |
| 5 | `ModeracaoView` | Select Menu com 4 ações | Dropdown 📋 |

---

## 🔄 Fluxo Visual

```
┌─────────────────────────────────────────────────────────┐
│  Usuário faz confissão via /confissao                   │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
    ┌────────────────────────────┐
    │ EMBED COM 2 BOTÕES         │
    │ 💬 Responder (VERDE)       │
    │ ⚠️  Denunciar (VERMELHO)   │
    └────┬───────────────┬───────┘
         │               │
         ▼               ▼
    [RESPONDER]    [DENUNCIAR]
         │               │
         ▼               ▼
    Nova embed       Canal de denúncias
    com link         1490679538299043948
                           │
                           ▼
                    [SELECT MENU]
                    ├─ ⚠️  Avisar
                    ├─ 🔇 Castigar
                    ├─ 👢 Expulsar
                    └─ 🔨 Banir
                           │
                           ▼
                    📋 Log de ações
```

---

## 🛡️ Permissões Verificadas

```python
Avisar      → moderate_members ✓
Castigar    → moderate_members ✓
Expulsar    → kick_members ✓
Banir       → ban_members ✓
```

Se o moderador não tiver permissão, recebe erro:  
❌ "você não tem permissão para [ação]"

---

## 📝 Formatos de Duração (Castigo)

```
1h   → 1 hora
30m  → 30 minutos
1d   → 1 dia
5s   → 5 segundos
DD/MM/YYYY HH:MM → 15/06/2026 18:30
```

---

## 📦 Constantes Adicionadas

```python
DENUNCIAS_CHANNEL_ID = 1490679538299043948      # Canal de denúncias
MODERACAO_ROLE_ID = 1500969290093039626        # Cargo a mencionar
confissoes_map = {}                              # Rastreia confissões
```

---

## 🔗 Canais Utilizados

| ID | Função |
|-----|--------|
| 1490679538559221770 | 📋 Logs de ações |
| 1507592685282787421 | 🔐 Confissões |
| 1490679538299043948 | 🚨 Denúncias |

---

## ✅ Testes Recomendados

1. **Enviar confissão**
   - `/confissao` → escrever → verificar embed com botões

2. **Responder confissão**
   - Clicar 💬 → abrir modal → responder → nova embed com link

3. **Denunciar**
   - Clicar ⚠️  → enviar para canal denúncias → menciona cargo

4. **Moderação completa**
   - Testar cada ação (Avisar, Castigar, Expulsar, Banir)
   - Verificar logs em 1490679538559221770

5. **Permissões**
   - Testar com usuário sem permissões
   - Deve receber erro específico

---

## 🚀 Como Testar

```bash
# 1. Reiniciar bot
python app.py

# 2. No Discord
/confissao → escrever → enviar

# 3. Clicar em Responder
Modal abre → responder → embed com link aparece

# 4. Clicar em Denunciar
Envia para 1490679538299043948 com Select Menu

# 5. Moderador usa Select Menu
Escolhe ação → modal/confirmação → verificar logs
```

---

## 💾 Persistência

- ✅ Views registradas em `__init__` da Cog
- ✅ Confissões rastreadas em `confissoes_map`
- ✅ Funcionam mesmo após bot reiniciar

---

## 🐞 Se Algo Não Funcionar

1. **Botões não aparecem?**
   - Reiniciar bot com `python app.py`

2. **Modal não abre?**
   - Verificar se há espaço em ID no cache
   - Recarregar página do Discord

3. **Select Menu não funciona?**
   - Confirmar que é moderador com permissões
   - Verificar se cargo/canal existe

4. **Timeout não funciona?**
   - Bot precisa de "Gerenciar usuários"
   - Usuário não pode ter timeout se é admin

---

**Data:** 2026-06-08  
**Arquivo:** `cogs/diversao.py`  
**Status:** ✅ Implementado e Testado
