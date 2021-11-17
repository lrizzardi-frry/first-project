# Instalar o Flask primeiro antes de quaisquer ações com o arquivo.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_index():
  return render_template('index.html')


def api_response():
  from flask import jsonify
  if request.method == 'POST':
    return jsonify(**request.json)


@app.route('/dados', methods=['POST'])
def get_data_from_html():
  Emails11 = request.form['EMAIL']
  Emails12 = open("/Users/lukin/Desktop/Site - MEO/emails.txt", "a")
  print("O e-mail cadastrado foi: " + Emails11)
  Emails12.write(" " + Emails11 + ",")

  return render_template('index.html')


if __name__ == '__main__':
  app.run('localhost', 8000)

# Aplicação para armazenar dados de input de email de um website num arquivo de texto.

# Versão do Python utilizada para o desenvolvimento da aplicação: Python 3.9