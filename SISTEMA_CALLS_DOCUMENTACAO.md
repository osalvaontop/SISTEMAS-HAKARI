# 🎙️ Sistema de Calls Personalizado - Documentação

## 📋 Visão Geral

Sistema completo de gerenciamento de calls de voz personalizado para o bot Discord. Permite que usuários criem, configurem e gerenciem seus próprios canais de voz com nome, limite de pessoas e controle de privacidade.

---

## 🚀 Como Usar

### 1️⃣ **Enviar o Painel de Criação** (`/painelcall`)
**Permissão necessária:** Administrador

Envia um painel visual no canal configurado (ID: 1507595486889115698) com um botão para criar calls.

```
/painelcall
```

**Resultado:**
- Uma embed aparece no canal especificado
- Usuários podem clicar em "Criar Call" para criar suas calls

---

### 2️⃣ **Criar uma Call**
**Como usar:** Clique no botão "Criar Call" no painel

**O que acontece:**
- Um canal de voz é criado com o nome padrão: `Call de <seu_nome>`
- Os dados da call são salvos automaticamente
- Você recebe uma confirmação de sucesso

---

### 3️⃣ **Configurar a Call** (`/configcall`)
**Como usar:** Digite `/configcall` em qualquer canal de texto

Uma embed aparece com 3 botões de configuração:

#### 🔤 Botão "Nome"
- Abre um modal para digitar o novo nome
- Se deixar em branco, volta ao padrão: `Call de <seu_nome>`
- Máximo de 100 caracteres

#### 👥 Botão "Limite"
- Abre um modal para digitar um número
- Define o limite de pessoas na call
- Se deixar em branco ou digitar `0`, a call fica sem limite
- Aceita números de 0 a 999

#### 🔒 Botão "Pública"
- Alterna entre pública (🟢 verde) e privada (🔴 vermelho)
- **Pública:** Qualquer pessoa do servidor pode entrar
- **Privada:** Apenas você pode entrar
- O estado é salvo automaticamente

---

### 4️⃣ **Deletar a Call** (`/deletarcall`)
**Como usar:** Digite `/deletarcall` em qualquer canal de texto

- Deleta seu canal de voz
- Remove os dados da call
- Você recebe uma confirmação de sucesso

---

### 5️⃣ **Listar Calls Ativas** (`/listarcalls`)
**Permissão necessária:** Administrador

Lista todas as calls ativas no servidor com informações detalhadas:
- Nome da call
- Criador
- Limite de pessoas
- Status (Pública/Privada)
- Quantidade de pessoas conectadas

```
/listarcalls
```

---

## 📊 Estrutura de Dados

Os dados das calls são salvos em um arquivo JSON (`calls_data.json`) com a seguinte estrutura:

```json
{
  "user_id": {
    "channel_id": 1234567890,
    "nome": "Call de Usuario",
    "limite": 10,
    "publica": true,
    "criador": 9876543210
  }
}
```

**Campos:**
- `user_id`: ID único do usuário (chave primária)
- `channel_id`: ID do canal de voz criado
- `nome`: Nome atual da call
- `limite`: Limite de pessoas (0 = sem limite)
- `publica`: true = pública, false = privada
- `criador`: ID do criador (para referência)

---

## ⚙️ Configurações

### ID do Canal do Painel
Para alterar o canal onde o painel de criação é enviado, edite a constante no início do arquivo `cogs/calls.py`:

```python
PAINEL_CHANNEL_ID = 1507595486889115698  # Altere para seu ID
```

### Arquivo de Dados
Os dados são salvos em `calls_data.json` na raiz do projeto. Se o arquivo não existir, é criado automaticamente na primeira call.

---

## 🔐 Segurança e Permissões

### Permissões Necessárias

O bot precisa das seguintes permissões no servidor:
- ✅ Enviar Mensagens
- ✅ Incorporar Links
- ✅ Gerenciar Canais
- ✅ Gerenciar Permissões
- ✅ Mover Membros
- ✅ Mudar Nick

### Restrições

- **Comando `/painelcall`**: Apenas administradores podem usar
- **Comando `/listarcalls`**: Apenas administradores podem usar
- **Comando `/configcall`**: Apenas o criador da call pode usar
- **Botões de configuração**: Apenas o criador pode clicar
- **Modais**: Apenas respostas válidas são aceitas

---

## 📝 Exemplos de Uso

### Exemplo 1: Criar e Configurar uma Call

1. Admin executa `/painelcall` → Painel aparece no canal
2. Usuário clica em "Criar Call" → Call criada com nome padrão
3. Usuário executa `/configcall` → Abre menu de configuração
4. Usuário clica em "Nome" → Digita "Estudo de Python" → Call renomeada
5. Usuário clica em "Limite" → Digita "5" → Limite definido para 5 pessoas
6. Usuário clica em "Pública" → Call fica privada (botão fica vermelho)

### Exemplo 2: Gerenciar Múltiplas Calls

Admin executa `/listarcalls`:
```
📋 Calls Ativas

👤 João
Nome: Call de João
Limite: sem limite
Status: 🟢 Pública
Pessoas: 2

👤 Maria
Nome: Estudo de Python
Limite: 5 pessoa(s)
Status: 🔴 Privada
Pessoas: 1
```

---

## 🐛 Resolução de Problemas

### Problema: "Você já possui uma call ativa!"
**Solução:** Execute `/deletarcall` para deletar a call anterior, depois tente novamente.

### Problema: "Canal da call não encontrado!"
**Solução:** O canal foi deletado manualmente. Execute `/deletarcall` para limpar os dados.

### Problema: Botões não funcionam
**Solução:** Reinicie o bot. Execute `Ctrl+C` e rode o bot novamente.

### Problema: Modal não abre
**Solução:** Verifique se você tem permissão para fazer isso. Apenas o criador pode usar `/configcall`.

---

## 📚 Arquivo de Dados

O arquivo `calls_data.json` é criado automaticamente. **NÃO DELETE** durante a execução do bot. Se precisar resetar:

1. Pare o bot
2. Delete o arquivo `calls_data.json`
3. Reinicie o bot

---

## 🔄 Atualização Automática de Views

As views (botões e modals) são registradas automaticamente quando o bot inicia. Você não precisa fazer nada especial.

---

## 📌 Notas Importantes

- ✅ Todos os comandos estão disponíveis apenas como **slash commands** (`/`)
- ✅ Os dados são salvos em tempo real
- ✅ As views persistem entre reinicializações do bot
- ✅ Apenas o criador da call pode gerenciá-la
- ✅ Calls vazias não são deletadas automaticamente

---

## 📞 Suporte

Se encontrar problemas ou tiver sugestões, consulte o arquivo `calls.py` para entender melhor o funcionamento ou entre em contato com o desenvolvedor.

---

**Desenvolvido com ❤️ para o bot HAKARI-VOLTOU**
