# 🧪 Testes do Sistema de Calls

Use este guia para testar todos os recursos do sistema de calls.

---

## ✅ Teste 1: Enviar o Painel

**Comando:** `/painelcall`

**Esperado:**
- ✅ Aparece uma mensagem de confirmação "✅ Painel enviado com sucesso!"
- ✅ No canal 1507595486889115698, aparece uma embed com:
  - Título: "🎙️ Sistema de Calls Personalizado"
  - Um botão verde escrito "Criar Call"

**Falha se:**
- ❌ Erro de permissão
- ❌ Canal não encontrado
- ❌ Bot sem permissão para enviar mensagens

---

## ✅ Teste 2: Criar uma Call

**Ação:** Clique no botão "Criar Call"

**Esperado:**
- ✅ Um novo canal de voz é criado com o nome "Call de <seu_nome>"
- ✅ Você recebe a mensagem: "✅ Call criada com sucesso!"
- ✅ Você pode ver o canal na lista de canais de voz

**Falha se:**
- ❌ Erro "Você já possui uma call ativa!"
- ❌ Canal não é criado
- ❌ Erro de permissão do bot

---

## ✅ Teste 3: Configurar Nome da Call

**Ação:** Execute `/configcall` → Clique em "Nome"

**Esperado:**
- ✅ Um modal aparece com o título "Configurar Nome da Call"
- ✅ Um campo de texto para digitar o nome
- ✅ Você digita um nome e clica em "Submit"
- ✅ Mensagem: "✅ Nome da call alterado para: **<novo_nome>**"
- ✅ O canal é renomeado no Discord

**Testes de casos extremos:**
- ⚪ Deixar em branco → Volta ao padrão "Call de <seu_nome>"
- ⚪ Digitar 100+ caracteres → Aceita até 100 caracteres
- ⚪ Caracteres especiais (🎙️, @, #) → Funciona normalmente

**Falha se:**
- ❌ Modal não aparece
- ❌ Nome não é atualizado
- ❌ Erro ao salvar dados

---

## ✅ Teste 4: Configurar Limite de Pessoas

**Ação:** Execute `/configcall` → Clique em "Limite"

**Esperado:**
- ✅ Um modal aparece com o título "Configurar Limite de Pessoas"
- ✅ Um campo de número para digitar o limite
- ✅ Você digita um número (ex: 5) e clica em "Submit"
- ✅ Mensagem: "✅ Limite da call definido para: **5 pessoa(s)**"
- ✅ O canal tem limite de 5 pessoas

**Testes de casos extremos:**
- ⚪ Deixar em branco → Sem limite (limite = 0)
- ⚪ Digitar 0 → Sem limite
- ⚪ Digitar 999 → Funciona normalmente
- ⚪ Digitar número negativo → Erro: "❌ O limite não pode ser negativo!"
- ⚪ Digitar texto → Erro: "❌ Digite um número válido!"

**Falha se:**
- ❌ Modal não aparece
- ❌ Limite não é aplicado
- ❌ Validação não funciona

---

## ✅ Teste 5: Alternar Privacidade (Pública/Privada)

**Ação:** Execute `/configcall` → Clique em "Pública"

**Primeira clicada (tornar privada):**
- ✅ Botão fica vermelho com label "Privada"
- ✅ Mensagem: "✅ Call definida como **🔴 Privada**"
- ✅ Apenas você pode entrar na call
- ✅ Outros usuários não conseguem conectar (permissão negada)

**Segunda clicada (tornar pública):**
- ✅ Botão fica verde com label "Pública"
- ✅ Mensagem: "✅ Call definida como **🟢 Pública**"
- ✅ Qualquer pessoa do servidor pode entrar
- ✅ Permissões são resetadas

**Falha se:**
- ❌ Botão não muda de cor
- ❌ Permissões não são aplicadas
- ❌ Outros usuários conseguem/não conseguem entrar quando deveriam

---

## ✅ Teste 6: Deletar a Call

**Comando:** `/deletarcall`

**Esperado:**
- ✅ Mensagem: "✅ Call deletada com sucesso!"
- ✅ O canal de voz é deletado do Discord
- ✅ Os dados são removidos do arquivo JSON

**Falha se:**
- ❌ Erro "Você não possui uma call ativa!"
- ❌ Canal não é deletado
- ❌ Dados não são removidos

---

## ✅ Teste 7: Listar Calls Ativas

**Comando:** `/listarcalls`

**Esperado:**
- ✅ Uma embed aparece com título "📋 Calls Ativas"
- ✅ Para cada call ativa, mostra:
  - Criador (nome do usuário)
  - Nome da call
  - Limite de pessoas
  - Status (Pública/Privada)
  - Quantidade de pessoas conectadas
- ✅ Se não houver calls: "📭 Nenhuma call ativa no momento."

**Falha se:**
- ❌ Erro de permissão
- ❌ Calls não aparecem
- ❌ Informações incorretas

---

## ✅ Teste 8: Múltiplas Calls

**Ação:** Dois usuários criam calls

**Esperado:**
- ✅ Ambos conseguem criar suas calls
- ✅ Cada um tem dados separados
- ✅ `/listarcalls` mostra as duas calls
- ✅ Configurações de uma não afetam a outra

**Falha se:**
- ❌ Usuário B recebe erro ao criar call
- ❌ Dados são misturados
- ❌ Configurações afetam múltiplas calls

---

## ✅ Teste 9: Comportamento Quando Call Já Existe

**Ação:** Tente criar outra call quando já tem uma ativa

**Esperado:**
- ✅ Mensagem: "❌ Você já possui uma call ativa! Delete-a primeiro."
- ✅ Nenhuma nova call é criada

**Falha se:**
- ❌ Segunda call é criada
- ❌ Mensagem não aparece

---

## ✅ Teste 10: Dados Persistem Após Restart

**Ação:**
1. Crie uma call com nome personalizado
2. Reinicie o bot
3. Execute `/configcall`

**Esperado:**
- ✅ Os botões ainda funcionam
- ✅ Os dados da call são mantidos
- ✅ Nome e limite são preservados

**Falha se:**
- ❌ Botões não funcionam após restart
- ❌ Dados são perdidos
- ❌ Arquivo JSON não é carregado

---

## 📊 Resumo de Testes

| Teste | Status | Notas |
|-------|--------|-------|
| 1 - Enviar Painel | ⬜ | |
| 2 - Criar Call | ⬜ | |
| 3 - Config Nome | ⬜ | |
| 4 - Config Limite | ⬜ | |
| 5 - Privacidade | ⬜ | |
| 6 - Deletar Call | ⬜ | |
| 7 - Listar Calls | ⬜ | |
| 8 - Múltiplas Calls | ⬜ | |
| 9 - Validação Duplicada | ⬜ | |
| 10 - Persistência Dados | ⬜ | |

**Legenda:**
- ⬜ = Não testado
- ✅ = Passou
- ❌ = Falhou

---

## 🔍 Checks Adicionais

### Verificar Arquivo de Dados
1. Crie uma call
2. Verifique se o arquivo `calls_data.json` foi criado na raiz do projeto
3. Abra com um editor de texto
4. Verifique se os dados estão corretos:
   ```json
   {
     "seu_id": {
       "channel_id": 123456789,
       "nome": "Call de Você",
       "limite": 0,
       "publica": true,
       "criador": seu_id
     }
   }
   ```

### Verificar Permissões
1. O bot deve ter as seguintes permissões:
   - ✅ Enviar Mensagens
   - ✅ Incorporar Links
   - ✅ Gerenciar Canais
   - ✅ Gerenciar Permissões
   - ✅ Mover Membros

### Verificar Sincronização de Comandos
1. Reinicie o bot
2. Verifique o console para a mensagem:
   ```
   ✅ X slash commands sincronizados!
   ```

---

## 🐛 Problemas Comuns e Soluções

| Problema | Solução |
|----------|---------|
| Comandos não aparecem | Reinicie o bot e aguarde 30s |
| Botões não funcionam | Reinicie o bot |
| Permissão negada | Verifique permissões do bot |
| Modal não abre | Verifique se é o criador |
| Dados perdidos | Backup do calls_data.json |

---

**Quando você terminar todos os testes, marque com ✅ na tabela acima!**
