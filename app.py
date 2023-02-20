from flask import Flask, redirect, render_template, request, session, url_for

from .secrets_keys import SECRET_KEY_SESSION

app = Flask(__name__)
app.secret_key = SECRET_KEY_SESSION


@app.route("/")
def homepage(
    mensagem_sucesso: str | None = None,
    error: str | None = None
):
    if session["usuario"] is not None:
        seasson = True
        mensagem_sucesso = "Seja bem vindo, " + session["usuario"]
        return render_template("index.html",
                               mensagem_sucesso=mensagem_sucesso,
                               seasson=seasson)
    else:
        return render_template("index.html")
    # Importar templates/index.html


@ app.route("/login", methods=["GET", "POST"])
def login(
    mensagem_sucesso: str | None = None,
    error: str | None = None,
    seasson: str | None = None,
):
    # Caso seja um post, fazer o login
    # Caso seja um get, importar templates/login.html
    if request.method == "POST":
        # Salvar o usuário na sessão
        # Verificar se o usuário existe e se a senha está correta

        if request.form["inputName"] == "admin" and \
                request.form["inputPassword"] == "adminadmin":
            session["usuario"] = request.form["inputName"]
            return redirect(url_for("homepage"))

        # Fazer o login
        # Se o login for bem sucedido, redirecionar para a página inicial
        # Se o login falhar, redirecionar para a página de login
        if True:
            mensagem_sucesso = "Login realizado com sucesso!"
            return render_template("index.html",
                                   mensagem_sucesso=mensagem_sucesso)
        else:
            error = "Erro ao realizar o login"
            return render_template("login.html", error=error)

    else:
        return render_template("login.html")


@app.route("/logout")
def logout(
    # Avisar o tipo de session
    mensagem_sucesso: str | None = None,
    error: str | None = None,
    seasson: bool | None = None
):
    if session["usuario"] is not None:
        mensagem_sucesso = "Logout realizado com sucesso! Volte sempre!"
        session["usuario"] = None
        seasson = False
        # Mensagem de sucesso no logout indo para o homepage
        return render_template("index.html",
                               mensagem_sucesso=mensagem_sucesso,
                               seasson=seasson)
    else:
        return render_template("index.html",
                               mensagem_sucesso='Você não estava logado!')


@ app.route("/loja")
def homepageloja():
    # Importar templates/index.html
    return render_template("index.html")


@ app.route("/sobre")
def sobre():
    # Importar templates/index.html
    return render_template("sobre.html")


@ app.route("/help")
def precisa_ajuda():
    # Importar templates/index.html
    return render_template("help.html")


@ app.route("/contato")
def contato():
    # Importar templates/index.html
    return render_template("contato.html")


@ app.route("/cadastro", methods=["GET", "POST"])
def cadastro(
    mensagem_sucesso: str | None = None,
    error: str | None = None,
):
    # Importar templates/index.html
    if request.method == "POST":
        # Fazer o cadastro
        # Se o cadastro for bem sucedido, redirecionar para a página inicial
        # Se o cadastro falhar, redirecionar para a página de cadastro
        if True:
            mensagem_sucesso = "Cadastro realizado com sucesso!"
            return render_template("index.html",
                                   mensagem_sucesso=mensagem_sucesso)
        else:
            error = "Erro ao realizar o cadastro"
            return render_template("cadastro.html", error=error)
    return render_template("cadastro.html",
                           mensagem_sucesso=mensagem_sucesso)
