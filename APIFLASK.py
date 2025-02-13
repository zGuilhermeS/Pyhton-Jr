from flask import Flask, request, jsonify # Importa as bibliotecas necessárias do Flask

app = Flask(__name__) # Cria a aplicação Flask

@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'Mundo') # Obtém o parâmetro 'nome' da URL, padrão "Mundo"
    return jsonify({'mensagem': f'Olá, {nome}!'})

@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    resultado = dados['num1'] + dados['num2'] # Calcula a soma dos dois números
    return jsonify({'resultado': resultado})

if __name__ == '__main__': # Executa o servidor Flask quando o script for executado diretamente
    app.run(debug=True)