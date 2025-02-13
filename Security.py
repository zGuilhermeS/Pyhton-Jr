from flask import Flask, request, jsonify  # Importa o Flask para criar a API
from werkzeug.security import check_password_hash, generate_password_hash  # Importa funções para segurança das senhas

app = Flask(__name__)  # Inicializa o aplicativo Flask

# Dicionário para armazenar usuários (banco de dados)
usuarios = {
    'admin': generate_password_hash('senha_segura')  # Cria um hash seguro da senha
}

# Rota para login (POST)
@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint para autenticação de usuários.
    Espera um JSON no formato:
    {
        "username": "admin",
        "password": "senha_segura"
    }
    Retorna uma mensagem indicando sucesso ou falha na autenticação.
    """
    dados = request.get_json()  # Obtém os dados enviados no corpo da requisição

    # Obtém o usuário e senha enviados
    username = dados.get('username')
    password = dados.get('password')

    # Verifica se o usuário existe e se a senha está correta
    if username in usuarios and check_password_hash(usuarios[username], password):
        return jsonify({'mensagem': 'Acesso concedido'}), 200  # Retorna sucesso (HTTP 200)

    return jsonify({'mensagem': 'Acesso negado'}), 401  # Retorna falha na autenticação (HTTP 401)

# Executa a aplicação Flask
if __name__ == '__main__':
    app.run()
