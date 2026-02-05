from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection

app = Flask(__name__)
app.secret_key = "safecare_secret_key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM usuarios WHERE email = %s AND senha = %s",
            (email, senha)
        )
        usuario = cursor.fetchone()

        cursor.close()
        conn.close()

        if usuario:
            return redirect(url_for('home'))
        else:
            flash("E-mail ou senha inválidos.")

    return render_template('login.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        perfil = request.form['perfil']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha, perfil) VALUES (%s, %s, %s, %s)",
            (nome, email, senha, perfil)
        )

        conn.commit()
        cursor.close()
        conn.close()

        flash("Cadastro realizado com sucesso.")
        return redirect(url_for('login'))

    return render_template('cadastro.html')


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

