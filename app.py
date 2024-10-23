from flask import Flask, render_template, request, jsonify
import yagmail
import json

app = Flask(__name__)

# Carregar configurações de e-mail
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

EMAIL_USER = config['EMAIL_USER']
EMAIL_PASSWORD = config['EMAIL_PASSWORD']

# Configurar yagmail com a senha do app
yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)

@app.route('/')
def index():
    return 'API de Envio de E-mails com Template HTML!'

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        recipient = data['recipient']
        subject = data['subject']
        nome = data['nome']

        # Renderizar o template com os dados do usuário
        html_content = render_template('email_template.html', nome=nome)

        # Enviar o e-mail
        yag.send(to=recipient, subject=subject, contents=html_content)

        return jsonify({"message": "E-mail enviado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import yagmail
import json

app = Flask(__name__)

# Carregar configurações de e-mail
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

EMAIL_USER = config['EMAIL_USER']
EMAIL_PASSWORD = config['EMAIL_PASSWORD']

# Configurar yagmail com a senha do app
yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)

@app.route('/')
def index():
    return 'API de Envio de E-mails com Template HTML!'

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        recipient = data['recipient']
        subject = data['subject']
        nome = data['nome']

        # Renderizar o template com os dados do usuário
        html_content = render_template('email_template.html', nome=nome)

        # Enviar o e-mail
        yag.send(to=recipient, subject=subject, contents=html_content)

        return jsonify({"message": "E-mail enviado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
