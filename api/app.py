from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User
import os

app = Flask(__name__)

# Configurações de segurança e banco de dados
# Usa uma chave secreta aleatória para segurança
app.config['SECRET_KEY'] = os.urandom(24)
# Armazenar banco de dados em 'instance' para segurança
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'

# Inicializa o banco de dados
db.init_app(app)

# Configura o gerenciador de login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """Carrega o usuário a partir do seu ID."""
    return User.query.get(int(user_id))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Rota para registro de novos usuários."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verifica se o usuário já existe
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash('Usuário já existe!')
            return redirect(url_for('register'))

        new_user = User(username=username)
        new_user.set_password(password)  # Armazena a senha de forma segura
        db.session.add(new_user)
        db.session.commit()
        flash('Registrado com sucesso!')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Rota para login de usuários existentes."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        # Verifica se o usuário existe e se a senha está correta
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciais inválidas!')

    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    """Rota do dashboard que exige autenticação."""
    return f'Bem-vindo {current_user.username}!'


@app.route('/logout')
@login_required
def logout():
    """Rota para logout do usuário."""
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    # Cria o banco de dados se não existir
    with app.app_context():
        db.create_all()
    app.run()  # Inicia a aplicação Flask
