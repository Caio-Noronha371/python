from flask import Flask

app = Flask(__name__)

@app.route('/')
def aula():
    return'Um decorator em Python é uma função que recebe outra função como argumento para "envolver" seu comportamento, adicionando funcionalidades extras (como logs, travas de segurança ou cronometragem) sem modificar o código interno da função original.Para funcionar, ele se baseia em três requisitos principais:Funções de Primeira Classe: A capacidade de tratar funções como objetos (passá-las por parâmetro).Closures: A função interna (wrapper) deve conseguir acessar e "lembrar" da função original recebida no escopo externo.Sintaxe @: O uso do "açúcar sintático" acima da definição da função para aplicar a transformação de forma limpa.' 
   
if __name__ == '__main__':
    app.run(debug=True)
