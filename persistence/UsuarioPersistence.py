# coding=utf-8
from pip._vendor import requests
from form.UsuarioForm import UsuarioForm
from form.SenhaForm import SenhaForm
from django.core.mail import send_mail
from datetime import datetime
import bcrypt


def administrador_cadastra(usuario):
    form = UsuarioForm(usuario)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        status_ativacao = form.cleaned_data['status_ativacao']

        data = administrador_monta_json(nome, email, status_ativacao)

        form = requests.post('http://localhost:3000/usuario', json=data)
    else:
        form = "Campos de Usuario nao preenchidos corretamente"
        for i in range(10):
            print("ERROOOOOOOOOOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUUUUUUUUUUUUUUUU")

    return form


def suporte_cadastra(usuario):
    now = datetime.now()
    form = UsuarioForm(usuario)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        status_ativacao = form.cleaned_data['status_ativacao']
        empresa = form.cleaned_data['empresa']

        data = suporte_monta_json(nome, email, empresa, status_ativacao)
        send_mail(
            'Novo Usuário em TW314',
            'Olá,' + nome + '! Esse e-mail foi cadastrado em nosso sistema em ' + now.day + '/' + now.month + '/' + now.year + ' às ' + now.hour + ':' + now.minute + 'hrs. Para continuar e acessar sua conta no sistema TW314, entre nesse link -link lindo aqui- e cadastre sua senha. Se acredita que houve um engano, por favor, entre em contado pelo link -link lindo aqui-. Time TW314',
            'fakedahalu@gmail.com',
            [email],
            fail_silently=False,
        )
        form = requests.post('http://localhost:3000/usuario', json=data)
    else:
        form = "<h3>Campos de Usuario nao preenchidos corretamente</h3>"

    return form


def atualiza(servico, pk):
    pass


def adiciona_senha(usuario_novo, pk):
    form = SenhaForm(usuario_novo)

    if form.is_valid():
        senha = "{}".format(form.cleaned_data['senha']).encode()
        senha_hash = bcrypt.hashpw(senha, bcrypt.gensalt())

        data = senha_monta_json(senha_hash)
        for i in range(10):
            print(data)

        try:
            form = requests.put('http://localhost:3000/servico/' + pk, json=data)

        except requests.exceptions.ConnectionError:  # verificar se funciona
            form = "Erro ao tentar conectar com WebService"

    return form


def lista_por_empresa_perfil(empresa, perfil):
    usuario = requests.get('http://localhost:3000/usuario/empresa/' + empresa + "&" + perfil).json()
    return usuario


def lista_por_perfil(perfil):
    return requests.get('http://localhost:3000/usuario/perfil/' + str(perfil)).json()


def suporte_monta_json(nome, email, empresa, status_ativacao):
    data = {'nome': nome, 'email': email, 'status_ativacao': status_ativacao, 'empresaId': empresa, 'perfilId': 2}
    return data


def senha_monta_json(senha):
    data = {'senha': senha}
    return data


def administrador_monta_json(nome, email, status_ativacao, data_inativacao):
    data = {'nome': nome, 'email': email, 'status_ativacao': status_ativacao, 'data_inativacao': data_inativacao,
            'perfilId': 3, 'empresaId': 1}

    return data
