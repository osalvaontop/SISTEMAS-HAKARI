# ⚡ GUIA RÁPIDO - NOVO SISTEMA DE CONFISSÃO

## 🎮 Para Usuários

### Enviar Confissão
```
/confissao
→ Escrever texto (até 4000 caracteres)
→ Enviar
→ Embed aparece no canal de confissões
```

### Responder Confissão
```
Ver confissão no canal
→ Clicar no botão 💬 "Responder"
→ Abrir modal de resposta
→ Escrever resposta (até 4000 caracteres)
→ Enviar
→ Nova embed aparece com link para confissão original
```

### Denunciar Confissão
```
Ver confissão inapropriada
→ Clicar no botão ⚠️ "Denunciar"
→ Mensagem aparece no canal 1490679538299043948
→ Moderadores são notificados
```

---

## 👨‍⚖️ Para Moderadores

### Receber Denúncia
```
Mensagem aparece no canal 1490679538299043948
→ Cargo @Moderadores é mencionado
→ Embed mostra confissão denunciada
→ Select Menu "abrir caso de moderação" disponível
```

### ⚠️ Avisar Usuário
```
Select Menu → Avisar
→ Abre modal para escrever motivo
→ Bot tenta enviar DM
→ Se DM fechada, publica no chat
→ Ação registrada em logs
```

### 🔇 Castigar Usuário (Mute)
```
Select Menu → Castigar
→ Abre modal para tempo
→ Inserir: 1h, 30m, 1d, 5s ou DD/MM/YYYY HH:MM
→ Bot aplica timeout
→ Ação registrada em logs

⏱️ Exemplos válidos:
  • 1h     (1 hora)
  • 30m    (30 minutos)
  • 1d     (1 dia)
  • 5s     (5 segundos)
  • 15/06/2026 18:30  (data e hora específica)
```

### 👢 Expulsar Usuário
```
Select Menu → Expulsar
→ Usuário é removido do servidor
→ Ação registrada em logs
⚠️ Requer permissão: kick_members
```

### 🔨 Banir Usuário
```
Select Menu → Banir
→ Usuário é banido permanentemente
→ Ação registrada em logs
⚠️ Requer permissão: ban_members
```

---

## 🔑 Permissões Necessárias

Para usar cada função, o moderador precisa ter:

| Ação | Permissão |
|------|-----------|
| Avisar | moderate_members |
| Castigar | moderate_members |
| Expulsar | kick_members |
| Banir | ban_members |

Se não tiver a permissão: ❌ "você não tem permissão para [ação]"

---

## 📱 Onde Tudo Acontece

```
Canal de Confissões (1507592685282787421)
  ↓
  Confissão aparece com botões
    ├─ Usuários clicam "Responder" → nova embed
    └─ Usuários clicam "Denunciar" →
              ↓
    Canal de Denúncias (1490679538299043948)
      ↓
      Cargo @Moderadores mencionado
      ↓
      Moderadores abrem Select Menu
      ↓
      Escolhem ação (Avisar/Castigar/Expulsar/Banir)
      ↓
    Tudo é registrado em Logs (1490679538559221770)
```

---

## 🆘 Problemas Comuns

| Problema | Solução |
|----------|---------|
| Botões não aparecem | Reiniciar bot com `python app.py` |
| Modal não abre ao clicar | Recarregar Discord (F5) |
| "Sem permissão" ao moderar | Pedir ao admin para dar a permissão necessária |
| DM do aviso não chegou | Bot enviará no canal de confissões |
| Timeout não funciona | Verificar se bot tem "Gerenciar usuários" |

---

## 📝 Exemplo Completo

```
1. João envia: /confissao → "tenho medo de errar"

2. Maria vê e clica "Responder"
   → escreve: "todos temos! é normal"
   → nova embed aparece com link

3. Carlos acha inapropriado e clica "Denunciar"
   → mensagem vai para canal de denúncias
   → @Moderadores é mencionado

4. Admin vê, abre Select Menu e escolhe "Banir"
   → João é banido
   → log é registrado em 1490679538559221770
```

---

## ✅ Checklist de Funcionalidades

- ✅ Confissões anônimas
- ✅ Responder confissões (visível quem respondeu)
- ✅ Denunciar confissões
- ✅ Avisar usuários (DM ou chat)
- ✅ Castigar com timeout (múltiplos formatos)
- ✅ Expulsar usuários
- ✅ Banir usuários
- ✅ Verificar permissões
- ✅ Registrar todas as ações

---

## 🚀 Iniciar

1. Reiniciar bot: `python app.py`
2. Testar comando: `/confissao`
3. Enviar confissão de teste
4. Testar botões (Responder e Denunciar)
5. Testar moderação com Select Menu

---

**Dúvidas?** Verificar `NOVO_SISTEMA_CONFISSOES_v2.md` para documentação completa.
