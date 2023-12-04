from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    # Envie os dados de login para a sua API usando requests
    login_url = 'http://127.0.0.1:5000/users/login'  # Substitua pela URL correta da sua API
    response = requests.post(login_url, json={'Email': email, 'Senha': senha})

    if response.ok:
        return 'Login successful'  # Aqui você pode redirecionar para outra página ou fazer outras ações necessárias
    else:
        return 'Login failed. Check your email and password.'

if __name__ == '__main__':
    app.run(debug=True, port=8000)
