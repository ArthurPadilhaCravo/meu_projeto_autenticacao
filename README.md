# Meu Projeto de Autenticação

## Descrição
Este projeto implementa um sistema de autenticação de usuários utilizando Flask, SQLAlchemy e Flask-Login.

## Funcionalidades
- Registro de usuários
- Login de usuários
- Logout
- Dashboard protegido

## Melhorias de Segurança
- As senhas dos usuários são armazenadas de forma segura utilizando `werkzeug.security`.
- A chave secreta é gerada aleatoriamente, aumentando a segurança da aplicação.
- O banco de dados é armazenado em um diretório separado (`instance`) para proteger dados sensíveis.

## Como Executar
1. Clonar o repositório.
2. Criar e ativar um ambiente virtual.
3. Instalar as dependências com `pip install -r requirements.txt`.
4. Executar a aplicação com `python app.py`.
