# Configurações do Sistema de Calls
# Este arquivo permite customizar o comportamento do sistema

# ==========================
# CONFIGURAÇÕES DO PAINEL
# ==========================

# ID do canal onde o painel de criação de calls será enviado
PAINEL_CHANNEL_ID = 1507595486889115698

# Título da embed do painel
PAINEL_TITULO = "🎙️ Sistema de Calls Personalizado"

# Descrição da embed do painel
PAINEL_DESCRICAO = "Clique no botão abaixo para criar sua call personalizada!"

# Cor da embed do painel (em hexadecimal)
# Exemplos: 0x0099ff (azul), 0xff0000 (vermelho), 0x00ff00 (verde)
PAINEL_COR = 0x0099ff

# ==========================
# CONFIGURAÇÕES DE CRIAÇÃO
# ==========================

# Nome padrão para novas calls
# Use {username} como placeholder para o nome do usuário
NOME_PADRAO_CALL = "Call de {username}"

# Limite padrão de pessoas na call (0 = sem limite)
LIMITE_PADRAO = 0

# ==========================
# CONFIGURAÇÕES DE MODAIS
# ==========================

# Título do modal de nome
MODAL_NOME_TITULO = "Configurar Nome da Call"

# Label do campo de nome
MODAL_NOME_LABEL = "Nome da Call"

# Placeholder do campo de nome
MODAL_NOME_PLACEHOLDER = "Digite o novo nome (deixe em branco para padrão)"

# Máximo de caracteres no nome
MODAL_NOME_MAX_CHARS = 100

# Título do modal de limite
MODAL_LIMITE_TITULO = "Configurar Limite de Pessoas"

# Label do campo de limite
MODAL_LIMITE_LABEL = "Limite de Pessoas"

# Placeholder do campo de limite
MODAL_LIMITE_PLACEHOLDER = "Digite o número (deixe em branco para sem limite)"

# Máximo de caracteres no limite (número)
MODAL_LIMITE_MAX_CHARS = 3

# ==========================
# CONFIGURAÇÕES DE BOTÕES
# ==========================

# Label dos botões
BOTAO_CRIAR_CALL = "Criar Call"
BOTAO_NOME = "Nome"
BOTAO_LIMITE = "Limite"
BOTAO_PUBLICA = "Pública"

# ==========================
# MENSAGENS DO SISTEMA
# ==========================

# Mensagens de sucesso
MSG_SUCESSO_CRIAR = "✅ Call criada com sucesso!"
MSG_SUCESSO_NOME = "✅ Nome da call alterado para: **{nome}**"
MSG_SUCESSO_LIMITE = "✅ Limite da call definido para: **{limite}**"
MSG_SUCESSO_PUBLICA = "✅ Call definida como **{status}**"
MSG_SUCESSO_DELETAR = "✅ Call deletada com sucesso!"
MSG_SUCESSO_PAINEL = "✅ Painel enviado com sucesso!"

# Mensagens de erro
MSG_ERRO_JA_EXISTE = "❌ Você já possui uma call ativa! Delete-a primeiro."
MSG_ERRO_NAO_EXISTE = "❌ Você não possui uma call ativa!"
MSG_ERRO_CANAL_NAO_ENCONTRADO = "❌ Canal da call não encontrado!"
MSG_ERRO_LIMITE_NEGATIVO = "❌ O limite não pode ser negativo!"
MSG_ERRO_LIMITE_INVALIDO = "❌ Digite um número válido!"
MSG_ERRO_NUMERO_INVALIDO = "❌ Digite um número válido!"
MSG_ERRO_GENERICO = "❌ Erro: {erro}"

# ==========================
# ARQUIVO DE DADOS
# ==========================

# Nome do arquivo para armazenar dados das calls
CALLS_DATA_FILE = "calls_data.json"

# ==========================
# COMPORTAMENTO DO SISTEMA
# ==========================

# Deletar calls vazias automaticamente após X minutos (0 = desativado)
DELETAR_CALLS_VAZIAS_APOS_MINUTOS = 0

# Registrar logs de criação/deleção de calls
ATIVAR_LOGS = True

# ==========================
# CORES DOS BOTÕES
# ==========================

# Cores dos botões de configuração
# Opções: blurple, gray, green, red, secondary, success, danger, link
COR_BOTAO_NOME = "blurple"
COR_BOTAO_LIMITE = "blurple"
COR_BOTAO_PUBLICA_ATIVO = "green"      # Quando pública
COR_BOTAO_PUBLICA_INATIVO = "red"      # Quando privada
