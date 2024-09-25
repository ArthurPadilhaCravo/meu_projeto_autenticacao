from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """Modelo de usuário para o banco de dados."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    # A senha é armazenada de forma segura
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Define a senha de forma segura."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica se a senha informada está correta."""
        return check_password_hash(self.password_hash, password)
