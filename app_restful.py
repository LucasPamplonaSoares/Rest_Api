from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json



app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0,
     'nome': 'Lucas',
     'habilidade': ['Python', 'Flask']
     },
    {'id': 1,
     'nome': 'Soares',
     'habilidade': ['Java', 'PHP']}
]

# Devolve o desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Proceuro o Administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response
    
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem':'Registro excluido'}
    
    
# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicaos]

# ROTAS #    
api.add_resource(Desenvolvedor, '/dev/<int:id>/') 
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)