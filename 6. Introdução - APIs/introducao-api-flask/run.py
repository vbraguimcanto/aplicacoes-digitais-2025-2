from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/victor')
def index():
    return 'Bem-vindo à sua API simples com Flask!'

@app.route('/api/exemplo', methods=['GET','POST'])
def exemplo():
    dados = {'mensagem': 'Resposta de exemplo da sua API'}
    return jsonify(dados), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/parametro', methods=['GET'])
def exemplo_parametro():
    nome = request.args.get('nome', 'Visitante')
    dados = {'mensagem': f'Olá, {nome}!'}
    return jsonify(dados), 200

@app.route('/api/payload', methods=['POST'])
def receber_payload():
    try:
        payload = request.get_json()
        return jsonify({"mensagem": "Payload recebido com sucesso", "payload": payload}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)