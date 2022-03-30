from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Lucas',
     'habilidade': ['Python', 'Flask']}
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])  # PUT para alterar
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Proceuro o Administrador da API'
            response =
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.load(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'messagem': 'Registro excluido'})


if __name__ == '__main__':
    app.run(debug=True)
